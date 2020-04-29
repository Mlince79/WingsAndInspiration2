from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Denisse Olsson',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2020'
    },
    {
        'author': 'Marisol Lince',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'April 27, 2020'
    },
]

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/about')
def aboutMe():
    return render_template('about.html')


@app.route('/events')
def events():
    return render_template('events.html')


@app.route('/coaching')
def myCoaching():
    return render_template('coaching.html')


@app.route('/blog')
def blog():
    return render_template('blog.html', posts=posts, title='blog')


if __name__ == '__main__':
    app.run(debug=True)
