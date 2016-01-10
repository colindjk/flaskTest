# Import Flask class from the flask module
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
# import sqlite3

# create the application object
app = Flask(__name__)

# config
import os
app.config.from_object(os.environ['APP_SETTINGS'])

# create the sqlalchemy object
db = SQLAlchemy(app)

from models import * # Can only be done once the 'db' has been created.

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    posts = db.session.query(BlogPost).all()
    return render_template('index.html', posts=posts)
    # posts = []
    # try:
        # # return "Hello, world!"
        # g.db = connect_db()
        # cur = g.db.execute('select * from posts')
        # # The below line of code is a one line for loop, and will be uncommented upon
        # # gaining a better understanding a python.
        # # posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
        # for row in cur.fetchall():
            # posts.append(dict(title=row[0], description=row[1]))
        # g.db.close()
    # except sqlite3.OperationalError:
        # flash("You do not have a database, fix that.")

@app.route('/welcome')
def welcome():
    return render_template("welcome.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('You were just logged in!')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You were just logged out!')
    return redirect(url_for('welcome'))

if __name__ == '__main__':
    app.run()

