from app import app
from app.forms import LoginForm

from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'Hulk'},
            'body': 'Beautiful day in Greenland'
        },
        {
            'author': {'username': 'Iron Man'},
            'body': 'The New York Knicks are pretty cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('login')
def 