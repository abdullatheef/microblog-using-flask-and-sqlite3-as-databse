import sqlite3 as lite
#from flask import request
import sys
con=lite.connect("blog.db")
with con:
	cur=con.cursor()
	cur.execute("DROP TABLE IF EXISTS posts")
	cur.execute("CREATE TABLE posts(id integer primary key autoincrement,title TEXT,text INT)")
#	cur.executemany("INSERT INTO sale VALUES(?,?)",[a['title'],a['text']])

