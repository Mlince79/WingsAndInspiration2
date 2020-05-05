import os 
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'pWvqv5fjeeeLdE9'


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
@app.route('/home')
def home():
    return render_template('home.html')


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
    return render_template(
        'blog.html', posts=posts, title='blog')



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('blog'))
    return render_template(
        'register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template(
        'login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP', "0.0.0.0"),
            port=int(os.environ.get('PORT', "5000")),
            debug=True)



