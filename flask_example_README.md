# Flask Example Application

This is a simple Flask web application that demonstrates basic Flask concepts including routing, templates, and form handling.

## Features

- Home page displaying a list of books
- Individual book detail pages
- About page with information about Flask
- Add new book functionality
- Responsive design with custom CSS

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install the required packages:
   ```
   pip install -r flask_requirements.txt
   ```

## Running the Application

1. Run the application:
   ```
   python flask_example.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5001`

## Application Structure

```
flask_example/
│
├── flask_example.py        # Main Flask application
├── flask_requirements.txt  # Python package dependencies
├── flask_example_README.md # This file
├── flask_tutorial.html     # Comprehensive Flask tutorial
├── templates/              # HTML templates
│   ├── flask_base.html     # Base template with common layout
│   ├── flask_index.html    # Home page template
│   ├── flask_about.html    # About page template
│   ├── flask_book.html     # Individual book template
│   └── flask_add_book.html # Add book form template
│
└── static/                 # Static files (CSS, JS, images)
    ├── css/
    ├── js/
    └── images/
```

## Flask Concepts Demonstrated

### 1. Routing
Routes are defined using the `@app.route()` decorator:
```python
@app.route('/')
def home():
    return render_template('flask_index.html', books=books)
```

### 2. Templates
Templates use Jinja2 syntax and are rendered with `render_template()`:
```python
return render_template('flask_index.html', books=books)
```

### 3. Template Inheritance
Base templates can be extended:
```html
{% extends "flask_base.html" %}
{% block content %}
<!-- Page specific content -->
{% endblock %}
```

### 4. Form Handling
Forms are processed in routes that accept multiple HTTP methods:
```python
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Process form data
```

### 5. URL Generation
URLs are generated using the `url_for()` function:
```html
<a href="{{ url_for('home') }}">Home</a>
```

## Learning Resources

- [Flask Official Documentation](https://flask.palletsprojects.com/)
- [Flask Tutorial](https://flask.palletsprojects.com/en/2.3.x/tutorial/)
- [Comprehensive Flask Tutorial (flask_tutorial.html)](flask_tutorial.html) - Included in this repository
