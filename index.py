import sqlite3
from flask import Flask,g

DATABASE = './database/data.db'
app = Flask(__name__)

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def hello_world():
	cur = get_db().cursor()
	cur.execute('SELECT * FROM tbl')
	print cur.fetchall()
	return 'Hello world'
if __name__ == '__main__':
	app.run(debug=True)

