import sqlite3
from flask import Flask,render_template,request

DATABASE = 'database/data.db'
app = Flask(__name__)


def get_db():
    db = sqlite3.connect(DATABASE)
    return db


@app.route('/index')
def show_entries():
    cur = get_db().cursor()
    cur.execute('SELECT * FROM tbl')
    print cur.fetchall()
    return render_template('index.html')
def valid_login(username,password):
    print 'username:'+username,'password:'+password
    return 1

@app.route('/login_process', methods=['GET', 'POST'])
def login_process():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            return render_template('index.html')
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)
@app.route('/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
