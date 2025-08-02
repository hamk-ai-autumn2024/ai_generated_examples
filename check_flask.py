try:
    import flask
    print("Flask is installed!")
    print("Flask version:", flask.__version__)
except ImportError:
    print("Flask is not installed. Please install it with: pip install flask")
