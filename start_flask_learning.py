"""
Flask Learning Starter Script
This script helps you get started with learning Flask by guiding you through the resources.
"""

import webbrowser
import os
import sys

def print_welcome():
    """Print a welcome message"""
    print("=" * 60)
    print("WELCOME TO FLASK LEARNING!")
    print("=" * 60)
    print()
    print("This script will help you get started with learning Flask.")
    print("You'll have access to tutorials, examples, and practical resources.")
    print()

def show_learning_paths():
    """Show the different learning paths available"""
    print("LEARNING PATHS:")
    print("-" * 20)
    print("1. Conceptual Learning (No installation required)")
    print("   - Read the comprehensive tutorial")
    print("   - Review concept explanations")
    print("   - Understand Flask without coding")
    print()
    print("2. Hands-On Practice (Installation required)")
    print("   - Install Flask on your system")
    print("   - Run and modify example applications")
    print("   - Build your own Flask projects")
    print()

def show_resources():
    """Show the key resources available"""
    print("KEY RESOURCES:")
    print("-" * 20)
    resources = [
        ("flask_tutorial.html", "Complete interactive tutorial"),
        ("flask_learning_summary.md", "Detailed concept explanations"),
        ("install_flask.html", "Step-by-step installation guide"),
        ("flask_example.py", "Practical example application"),
        ("index.html", "Navigation hub for all resources")
    ]
    
    for i, (file, description) in enumerate(resources, 1):
        print(f"{i}. {file} - {description}")
    print()

def open_resource():
    """Open a resource in the browser"""
    print("OPENING RESOURCES:")
    print("-" * 20)
    print("1. Open the main index (recommended starting point)")
    print("2. Open the comprehensive tutorial")
    print("3. Open the installation guide")
    print("4. Exit")
    print()
    
    choice = input("Enter your choice (1-4): ").strip()
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    if choice == "1":
        file_path = os.path.join(current_dir, "index.html")
        print(f"Opening index.html...")
    elif choice == "2":
        file_path = os.path.join(current_dir, "flask_tutorial.html")
        print(f"Opening flask_tutorial.html...")
    elif choice == "3":
        file_path = os.path.join(current_dir, "install_flask.html")
        print(f"Opening install_flask.html...")
    elif choice == "4":
        print("Goodbye!")
        return
    else:
        print("Invalid choice. Opening index.html by default...")
        file_path = os.path.join(current_dir, "index.html")
    
    if os.path.exists(file_path):
        webbrowser.open(f"file://{file_path}")
    else:
        print(f"Error: {os.path.basename(file_path)} not found!")

def show_next_steps():
    """Show next steps for learning Flask"""
    print("NEXT STEPS:")
    print("-" * 20)
    print("1. Install Flask on your system:")
    print("   - Follow the instructions in install_flask.html")
    print("   - Use a virtual environment (recommended)")
    print()
    print("2. Run the example application:")
    print("   - On Windows: Double-click run_flask_example.bat")
    print("   - On macOS/Linux: Run 'python flask_example.py'")
    print()
    print("3. Visit http://127.0.0.1:5001 in your browser")
    print()
    print("4. Start building your own Flask applications!")
    print()

def main():
    """Main function"""
    print_welcome()
    show_learning_paths()
    show_resources()
    show_next_steps()
    
    open_resource()

if __name__ == "__main__":
    main()
