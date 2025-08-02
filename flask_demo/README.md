# Flask Demo Application

This is a simple Flask web application that demonstrates basic Flask concepts including routing, templates, and form handling.

## Features

- Home page displaying a list of blog posts
- Individual post pages
- About page with information about Flask
- Create new post functionality
- Responsive design using Bootstrap

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
   pip install -r requirements.txt
   ```

## Running the Application

1. Set the FLASK_APP environment variable:
   ```
   export FLASK_APP=app.py  # On Windows: set FLASK_APP=app.py
   ```
2. Run the application:
   ```
   flask run
   ```
   
   Or alternatively:
   ```
   python app.py
   ```

3. Open your web browser and go to `http://127.0.0.1:5000`

## Application Structure

```
flask_demo/
│
├── app.py              # Main Flask application
├── requirements.txt    # Python package dependencies
├── README.md           # This file
├── templates/           # HTML templates
│   ├── base.html       # Base template with common layout
│   ├── home.html       # Home page template
│   ├── about.html      # About page template
│   ├── post.html       # Individual post template
│   └── create.html     # Create post form template
│
└── static/             # Static files (CSS, JS, images)
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
    return render_template('home.html', posts=posts)
```

### 2. Templates
Templates use Jinja2 syntax and are rendered with `render_template()`:
```python
return render_template('home.html', posts=posts)
```

### 3. Template Inheritance
Base templates can be extended:
```html
{% extends "base.html" %}
{% block content %}
<!-- Page specific content -->
{% endblock %}
```

### 4. Form Handling
Forms are processed in routes that accept multiple HTTP methods:
```python
@app.route('/create', methods=['GET', 'POST'])
def create():
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
