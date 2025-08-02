"""
Flask Example Application
This is a simple Flask application demonstrating core concepts.
"""

from flask import Flask, render_template, request, redirect, url_for

# Create the Flask application instance
app = Flask(__name__)

# Sample data for our application
books = [
    {
        'id': 1,
        'title': 'Flask Web Development',
        'author': 'Miguel Grinberg',
        'year': 2018
    },
    {
        'id': 2,
        'title': 'Python Crash Course',
        'author': 'Eric Matthes',
        'year': 2019
    },
    {
        'id': 3,
        'title': 'Automate the Boring Stuff with Python',
        'author': 'Al Sweigart',
        'year': 2015
    }
]

# Route for the home page
@app.route('/')
def home():
    return render_template('flask_index.html', books=books)

# Route for the about page
@app.route('/about')
def about():
    return render_template('flask_about.html')

# Route for individual books
@app.route('/book/<int:book_id>')
def book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return render_template('flask_book.html', book=book)
    else:
        return "Book not found", 404

# Route for adding a new book (GET and POST)
@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        author = request.form['author']
        year = int(request.form['year'])
        
        # Create new book
        new_book = {
            'id': len(books) + 1,
            'title': title,
            'author': author,
            'year': year
        }
        
        books.append(new_book)
        return redirect(url_for('home'))
    
    return render_template('flask_add_book.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=5001)
