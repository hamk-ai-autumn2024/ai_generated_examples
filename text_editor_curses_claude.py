#!/usr/bin/env python3
"""
Modern Console Text Editor
A comprehensive text editor that runs in the console using curses library.
Supports standard Windows keyboard shortcuts and file operations.
"""

import curses
import os
import sys
from typing import List, Tuple, Optional
from pathlib import Path

class TextEditor:
    """A comprehensive console-based text editor with Windows-style shortcuts."""
    
    # Constants for keyboard shortcuts
    CTRL_S = 19  # Save
    CTRL_O = 15  # Open
    CTRL_N = 14  # New
    CTRL_Q = 17  # Quit
    CTRL_X = 24  # Cut
    CTRL_C = 3   # Copy
    CTRL_V = 22  # Paste
    CTRL_Z = 26  # Undo
    CTRL_Y = 25  # Redo
    CTRL_A = 1   # Select All
    CTRL_F = 6   # Find
    
    def __init__(self):
        """Initialize the text editor."""
        self.lines: List[str] = [""]
        self.cursor_row: int = 0
        self.cursor_col: int = 0
        self.offset_row: int = 0
        self.offset_col: int = 0
        self.filename: Optional[str] = None
        self.modified: bool = False
        self.clipboard: str = ""
        self.status_message: str = ""
        self.screen = None
        self.height: int = 0
        self.width: int = 0
        
        # Undo/Redo stacks
        self.undo_stack: List[Tuple[List[str], int, int]] = []
        self.redo_stack: List[Tuple[List[str], int, int]] = []
        self.max_undo: int = 100
        
    def save_state(self):
        """Save current state for undo functionality."""
        state = (
            [line for line in self.lines],  # Deep copy of lines
            self.cursor_row,
            self.cursor_col
        )
        self.undo_stack.append(state)
        if len(self.undo_stack) > self.max_undo:
            self.undo_stack.pop(0)
        self.redo_stack.clear()
        
    def undo(self):
        """Undo the last action."""
        if self.undo_stack:
            current_state = (
                [line for line in self.lines],
                self.cursor_row,
                self.cursor_col
            )
            self.redo_stack.append(current_state)
            
            state = self.undo_stack.pop()
            self.lines, self.cursor_row, self.cursor_col = state
            self.modified = True
            self.status_message = "Undone"
            
    def redo(self):
        """Redo the last undone action."""
        if self.redo_stack:
            current_state = (
                [line for line in self.lines],
                self.cursor_row,
                self.cursor_col
            )
            self.undo_stack.append(current_state)
            
            state = self.redo_stack.pop()
            self.lines, self.cursor_row, self.cursor_col = state
            self.modified = True
            self.status_message = "Redone"
            
    def move_cursor(self, key: int):
        """Move cursor based on key input."""
        if key == curses.KEY_UP and self.cursor_row > 0:
            self.cursor_row -= 1
            self.cursor_col = min(self.cursor_col, len(self.lines[self.cursor_row]))
        elif key == curses.KEY_DOWN and self.cursor_row < len(self.lines) - 1:
            self.cursor_row += 1
            self.cursor_col = min(self.cursor_col, len(self.lines[self.cursor_row]))
        elif key == curses.KEY_LEFT and self.cursor_col > 0:
            self.cursor_col -= 1
        elif key == curses.KEY_RIGHT and self.cursor_col < len(self.lines[self.cursor_row]):
            self.cursor_col += 1
        elif key == curses.KEY_HOME:
            self.cursor_col = 0
        elif key == curses.KEY_END:
            self.cursor_col = len(self.lines[self.cursor_row])
            
    def scroll_screen(self):
        """Adjust screen offset to keep cursor visible."""
        # Vertical scrolling
        if self.cursor_row < self.offset_row:
            self.offset_row = self.cursor_row
        elif self.cursor_row >= self.offset_row + self.height - 2:
            self.offset_row = self.cursor_row - self.height + 3
            
        # Horizontal scrolling
        if self.cursor_col < self.offset_col:
            self.offset_col = self.cursor_col
        elif self.cursor_col >= self.offset_col + self.width - 1:
            self.offset_col = self.cursor_col - self.width + 2
            
    def insert_char(self, char: int):
        """Insert a character at the current cursor position."""
        if char == ord('\n') or char == curses.KEY_ENTER or char == 10:
            self.save_state()
            # Split line at cursor
            current_line = self.lines[self.cursor_row]
            self.lines[self.cursor_row] = current_line[:self.cursor_col]
            self.lines.insert(self.cursor_row + 1, current_line[self.cursor_col:])
            self.cursor_row += 1
            self.cursor_col = 0
            self.modified = True
        elif char == curses.KEY_BACKSPACE or char == 127 or char == 8:
            if self.cursor_col > 0:
                self.save_state()
                current_line = self.lines[self.cursor_row]
                self.lines[self.cursor_row] = current_line[:self.cursor_col-1] + current_line[self.cursor_col:]
                self.cursor_col -= 1
                self.modified = True
            elif self.cursor_row > 0:
                self.save_state()
                # Join with previous line
                prev_line_len = len(self.lines[self.cursor_row - 1])
                self.lines[self.cursor_row - 1] += self.lines[self.cursor_row]
                del self.lines[self.cursor_row]
                self.cursor_row -= 1
                self.cursor_col = prev_line_len
                self.modified = True
        elif char == curses.KEY_DC:  # Delete key
            if self.cursor_col < len(self.lines[self.cursor_row]):
                self.save_state()
                current_line = self.lines[self.cursor_row]
                self.lines[self.cursor_row] = current_line[:self.cursor_col] + current_line[self.cursor_col+1:]
                self.modified = True
            elif self.cursor_row < len(self.lines) - 1:
                self.save_state()
                # Join with next line
                self.lines[self.cursor_row] += self.lines[self.cursor_row + 1]
                del self.lines[self.cursor_row + 1]
                self.modified = True
        elif 32 <= char <= 126:  # Printable characters
            self.save_state()
            current_line = self.lines[self.cursor_row]
            self.lines[self.cursor_row] = current_line[:self.cursor_col] + chr(char) + current_line[self.cursor_col:]
            self.cursor_col += 1
            self.modified = True
            
    def copy_line(self):
        """Copy current line to clipboard."""
        if 0 <= self.cursor_row < len(self.lines):
            self.clipboard = self.lines[self.cursor_row]
            self.status_message = "Line copied"
            
    def cut_line(self):
        """Cut current line to clipboard."""
        if 0 <= self.cursor_row < len(self.lines):
            self.save_state()
            self.clipboard = self.lines[self.cursor_row]
            if len(self.lines) > 1:
                del self.lines[self.cursor_row]
                if self.cursor_row >= len(self.lines):
                    self.cursor_row = len(self.lines) - 1
            else:
                self.lines[0] = ""
            self.cursor_col = 0
            self.modified = True
            self.status_message = "Line cut"
            
    def paste_line(self):
        """Paste clipboard content."""
        if self.clipboard:
            self.save_state()
            self.lines.insert(self.cursor_row + 1, self.clipboard)
            self.cursor_row += 1
            self.cursor_col = 0
            self.modified = True
            self.status_message = "Line pasted"
            
    def save_file(self, filename: Optional[str] = None):
        """Save the current file."""
        try:
            if filename:
                self.filename = filename
            elif not self.filename:
                self.filename = self.prompt("Save as: ")
                if not self.filename:
                    self.status_message = "Save cancelled"
                    return False
                    
            with open(self.filename, 'w', encoding='utf-8') as f:
                for i, line in enumerate(self.lines):
                    f.write(line)
                    if i < len(self.lines) - 1:
                        f.write('\n')
                        
            self.modified = False
            self.status_message = f"Saved: {self.filename}"
            return True
        except Exception as e:
            self.status_message = f"Error saving: {str(e)}"
            return False
            
    def load_file(self, filename: str):
        """Load a file."""
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    content = f.read()
                    if content:
                        self.lines = content.splitlines()
                        if not self.lines:
                            self.lines = [""]
                    else:
                        self.lines = [""]
            else:
                self.lines = [""]
                
            self.filename = filename
            self.cursor_row = 0
            self.cursor_col = 0
            self.offset_row = 0
            self.offset_col = 0
            self.modified = False
            self.undo_stack.clear()
            self.redo_stack.clear()
            self.status_message = f"Loaded: {filename}"
            return True
        except Exception as e:
            self.status_message = f"Error loading: {str(e)}"
            return False
            
    def new_file(self):
        """Create a new file."""
        if self.modified:
            response = self.prompt("Save changes? (y/n): ")
            if response and response.lower() == 'y':
                if not self.save_file():
                    return False
                    
        self.lines = [""]
        self.filename = None
        self.cursor_row = 0
        self.cursor_col = 0
        self.offset_row = 0
        self.offset_col = 0
        self.modified = False
        self.undo_stack.clear()
        self.redo_stack.clear()
        self.status_message = "New file"
        return True
        
    def prompt(self, message: str) -> str:
        """Display a prompt and get user input."""
        try:
            self.screen.addstr(self.height - 1, 0, message)
            self.screen.clrtoeol()
            self.screen.refresh()
            
            curses.echo()
            curses.curs_set(1)
            
            # Get input
            response = self.screen.getstr(self.height - 1, len(message)).decode('utf-8')
            
            curses.noecho()
            curses.curs_set(0)
            
            return response
        except:
            curses.noecho()
            curses.curs_set(0)
            return ""
            
    def find_text(self):
        """Find text in the document."""
        search_term = self.prompt("Find: ")
        if not search_term:
            return
            
        # Search from current position
        for row in range(self.cursor_row, len(self.lines)):
            start_col = self.cursor_col + 1 if row == self.cursor_row else 0
            pos = self.lines[row].find(search_term, start_col)
            if pos != -1:
                self.cursor_row = row
                self.cursor_col = pos
                self.status_message = f"Found: {search_term}"
                return
                
        # Search from beginning
        for row in range(0, self.cursor_row + 1):
            end_col = self.cursor_col if row == self.cursor_row else len(self.lines[row])
            pos = self.lines[row].find(search_term, 0, end_col)
            if pos != -1:
                self.cursor_row = row
                self.cursor_col = pos
                self.status_message = f"Found: {search_term}"
                return
                
        self.status_message = f"Not found: {search_term}"
        
    def draw_screen(self):
        """Draw the editor screen."""
        self.screen.clear()
        
        # Draw text content
        for i in range(min(self.height - 2, len(self.lines) - self.offset_row)):
            row = i + self.offset_row
            if row < len(self.lines):
                line = self.lines[row]
                if self.offset_col < len(line):
                    display_line = line[self.offset_col:self.offset_col + self.width]
                else:
                    display_line = ""
                try:
                    self.screen.addstr(i, 0, display_line[:self.width-1])
                except curses.error:
                    pass
                    
        # Draw status line
        status_left = f"{self.filename or 'Untitled'}{' *' if self.modified else ''}"
        status_right = f"Line {self.cursor_row + 1}, Col {self.cursor_col + 1}"
        status_line = status_left + " " * (self.width - len(status_left) - len(status_right)) + status_right
        
        try:
            self.screen.addstr(self.height - 2, 0, status_line[:self.width-1], curses.A_REVERSE)
        except curses.error:
            pass
            
        # Draw message line
        if self.status_message:
            try:
                self.screen.addstr(self.height - 1, 0, self.status_message[:self.width-1])
            except curses.error:
                pass
                
        # Position cursor
        screen_row = self.cursor_row - self.offset_row
        screen_col = self.cursor_col - self.offset_col
        if 0 <= screen_row < self.height - 2 and 0 <= screen_col < self.width:
            try:
                self.screen.move(screen_row, screen_col)
            except curses.error:
                pass
                
        self.screen.refresh()
        
    def run(self):
        """Main editor loop."""
        try:
            # Initialize curses
            self.screen = curses.initscr()
            curses.noecho()
            curses.cbreak()
            curses.curs_set(1)
            self.screen.keypad(True)
            
            # Get screen dimensions
            self.height, self.width = self.screen.getmaxyx()
            
            # Main loop
            while True:
                self.scroll_screen()
                self.draw_screen()
                
                # Clear status message after displaying
                if self.status_message:
                    self.status_message = ""
                    
                key = self.screen.getch()
                
                # Handle keyboard shortcuts
                if key == self.CTRL_Q:  # Quit
                    if self.modified:
                        response = self.prompt("Save changes before quit? (y/n/c): ")
                        if response:
                            if response.lower() == 'y':
                                if self.save_file():
                                    break
                            elif response.lower() == 'n':
                                break
                            # 'c' or anything else cancels
                    else:
                        break
                elif key == self.CTRL_S:  # Save
                    self.save_file()
                elif key == self.CTRL_O:  # Open
                    filename = self.prompt("Open file: ")
                    if filename:
                        self.load_file(filename)
                elif key == self.CTRL_N:  # New
                    self.new_file()
                elif key == self.CTRL_C:  # Copy
                    self.copy_line()
                elif key == self.CTRL_X:  # Cut
                    self.cut_line()
                elif key == self.CTRL_V:  # Paste
                    self.paste_line()
                elif key == self.CTRL_Z:  # Undo
                    self.undo()
                elif key == self.CTRL_Y:  # Redo
                    self.redo()
                elif key == self.CTRL_F:  # Find
                    self.find_text()
                elif key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT,
                           curses.KEY_HOME, curses.KEY_END]:
                    self.move_cursor(key)
                elif key == curses.KEY_RESIZE:
                    self.height, self.width = self.screen.getmaxyx()
                else:
                    self.insert_char(key)
                    
        except KeyboardInterrupt:
            pass
        except Exception as e:
            # Restore terminal before showing error
            curses.endwin()
            print(f"Error: {str(e)}")
            sys.exit(1)
        finally:
            # Restore terminal
            try:
                curses.endwin()
            except:
                pass

def main():
    """Main function to start the text editor."""
    editor = TextEditor()
    
    # Load file from command line argument if provided
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        editor.load_file(filename)
        
    print("Modern Console Text Editor")
    print("Keyboard shortcuts:")
    print("  Ctrl+N: New file")
    print("  Ctrl+O: Open file")
    print("  Ctrl+S: Save file")
    print("  Ctrl+Q: Quit")
    print("  Ctrl+C: Copy line")
    print("  Ctrl+X: Cut line")
    print("  Ctrl+V: Paste line")
    print("  Ctrl+Z: Undo")
    print("  Ctrl+Y: Redo")
    print("  Ctrl+F: Find text")
    print("\nPress any key to start the editor...")
    input()
    
    editor.run()

if __name__ == "__main__":
    main()