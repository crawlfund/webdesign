import sqlite3
from flask import Flask,render_template,request

DATABASE = 'database/data.db'
app = Flask(__name__)


def get_db():
    db = sqlite3.connect(DATABASE)
    return db


@app.route('/va')
def show_entries():
    cur = get_db().cursor()
    #cur.execute('SELECT * FROM tbl')
    #print cur.fetchall()
    return render_template('index.html',valid=False)

def valid_login(username,password):
    if username==u'root' and password ==u'root':
        return True
    else:
        return False

@app.route('/login', methods=['GET', 'POST'])
def login_process():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            return render_template('index.html',valid=True)
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)
@app.route('/')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
