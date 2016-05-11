import sqlite3
from flask import Flask,render_template

DATABASE = '/Users/Joy/Code/webdesign/database/data.db'
app = Flask(__name__)

def get_db():
    db = sqlite3.connect(DATABASE)
    return db

@app.route('/')
def show_entries():
	cur = get_db().cursor()
	cur.execute('SELECT * FROM tbl')
	print cur.fetchall()
	return render_template('index.html')


@app.route('/login')
def login():
	return render_template('login.html')
if __name__ == '__main__':
	app.run(debug=True)

