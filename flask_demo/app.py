from flask import Flask, render_template, request, redirect, url_for

# Create the Flask application instance
app = Flask(__name__)

# Sample data for our application
posts = [
    {
        'id': 1,
        'title': 'First Post',
        'content': 'This is the content of the first post.',
        'author': 'John Doe',
        'date_posted': 'April 20, 2023'
    },
    {
        'id': 2,
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
        'author': 'Jane Smith',
        'date_posted': 'April 21, 2023'
    }
]

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html', posts=posts)

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for individual posts
@app.route('/post/<int:post_id>')
def post(post_id):
    post = next((post for post in posts if post['id'] == post_id), None)
    if post:
        return render_template('post.html', post=post)
    else:
        return "Post not found", 404

# Route for creating a new post (GET and POST)
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Get form data
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
        
        # Create new post
        new_post = {
            'id': len(posts) + 1,
            'title': title,
            'content': content,
            'author': author,
            'date_posted': 'Today'
        }
        
        posts.append(new_post)
        return redirect(url_for('home'))
    
    return render_template('create.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
