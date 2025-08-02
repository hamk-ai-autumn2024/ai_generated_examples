"""
Script to check if Flask is installed and provide installation instructions if not.
"""

def check_flask():
    try:
        import flask
        print("✓ Flask is installed!")
        print(f"  Version: {flask.__version__}")
        print("\nYou can now run the Flask example:")
        print("  python flask_example.py")
        return True
    except ImportError:
        print("✗ Flask is not installed.")
        print("\nTo install Flask, run:")
        print("  pip install flask")
        print("\nIf you're using a virtual environment (recommended):")
        print("  python -m venv venv")
        print("  venv\\Scripts\\activate  # On Windows")
        print("  source venv/bin/activate  # On macOS/Linux")
        print("  pip install flask")
        return False

if __name__ == "__main__":
    check_flask()
