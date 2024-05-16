from app import app
from app.forms import LoginForm

from flask import render_template, flash, redirect

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


@app.route('/login')
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data
        ))
        return redirect('/index')

    return render_template('login.html', title='Sign In', form=form)