"""
Flask Quickstart Example
This is a minimal Flask application to verify installation.
"""

# This is a simple Flask application that you can run to verify 
# that Flask is installed correctly.

# Note: This file will not run if Flask is not installed.
# You'll get an ImportError when trying to import Flask.

def flask_installation_check():
    """
    This function explains how to check if Flask is installed
    without actually trying to import it (which would cause an error
    if Flask isn't installed).
    """
    print("To check if Flask is installed, run this command in your terminal:")
    print("  python -c \"import flask; print(flask.__version__)\"")
    print("\nIf Flask is installed, you'll see the version number.")
    print("If Flask is not installed, you'll see an ImportError.")
    
    print("\nTo install Flask:")
    print("  pip install Flask")
    
    print("\nTo install Flask in a virtual environment:")
    print("  python -m venv venv")
    print("  venv\\Scripts\\activate  # On Windows")
    print("  source venv/bin/activate  # On macOS/Linux")
    print("  pip install Flask")

# Explanation of a minimal Flask application
FLASK_APP_EXAMPLE = '''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

if __name__ == '__main__':
    app.run(debug=True)
'''

print("Flask Quickstart Example")
print("========================")
print("\nThis script explains how to verify Flask installation.")
print("It does not actually import Flask to avoid errors.")
flask_installation_check()

print("\n" + "="*50)
print("FLASK APPLICATION EXAMPLE:")
print("="*50)
print(FLASK_APP_EXAMPLE)

print("\nTo run this Flask application:")
print("1. Save the code above in a file named app.py")
print("2. Run: python app.py")
print("3. Open your browser to http://127.0.0.1:5000")
