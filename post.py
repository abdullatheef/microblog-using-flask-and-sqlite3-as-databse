import sqlite3

from functools import wraps
from flask import *

import db

DATABASE = 'blog.db'

app=Flask(__name__)
app.config.from_object(__name__)


def connect_db():
	return sqlite3.connect(app.config['DATABASE'])


@app.route('/')

def a():
	g.db=connect_db()
	return render_template('new.html')

@app.route('/new1')
def b():
	return render_template('new1.html')

@app.route('/post',methods=['POST'])
def add_entry():
	g.db=connect_db()
	g.db.execute('insert into posts (title, text) values (?, ?)',[request.form['title'], request.form['text']])
	g.db.commit()
	return redirect(url_for('show_entries'))


@app.route('/post')
def show_entries():
	g.db=connect_db()
	cur = g.db.execute('select title, text from posts order by id desc')
	posts = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
	return render_template('post.html',posts=posts)

app.run(debug=True)


