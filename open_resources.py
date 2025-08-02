"""
Script to open Flask learning resources in the default browser.
"""

import webbrowser
import os

def open_flask_resources():
    """Open the main index file in the default browser"""
    
    # Get the current directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Path to the index.html file
    index_path = os.path.join(current_dir, "index.html")
    
    # Check if the file exists
    if os.path.exists(index_path):
        # Open in the default browser
        webbrowser.open(f"file://{index_path}")
        print("Opening Flask Learning Resources in your default browser...")
        print(f"File: {index_path}")
    else:
        print("Error: index.html not found!")
        print("Please make sure you're running this script from the correct directory.")

if __name__ == "__main__":
    open_flask_resources()
