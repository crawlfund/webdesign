#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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

@app.route('/chiyao')
def chiyao():
    cur=get_db().cursor()
    cur.execute('SELECT id,name,chiyao FROM information')
    title=u'服药情况'
    table_head=[u'编号',u'姓名',u'是否已服药']
    return render_template('index.html',valid=True,title=title,table_head=table_head,content=cur.fetchall())

@app.route('/weisheng')
def weisheng():
    cur=get_db().cursor()
    cur.execute('SELECT id,name,weisheng FROM information')
    title=u'卫生情况'
    table_head=[u'编号',u'姓名',u'是否已打扫']
    return render_template('index.html',valid=True,title=title,table_head=table_head,content=cur.fetchall())

@app.route('/qiuzhu')
def qiuzhu():
    cur=get_db().cursor()
    cur.execute('SELECT id,name,qiuzhu FROM information')
    title=u'求助情况'
    table_head=[u'编号',u'姓名',u'是否需要帮助']
    return render_template('index.html',valid=True,title=title,table_head=table_head,content=cur.fetchall())
@app.route('/qichuang')
def qichuang():
    cur=get_db().cursor()
    cur.execute('SELECT id,name,qichuang FROM information')
    title=u'起床情况'
    table_head=[u'编号',u'姓名',u'是否已起床']
    return render_template('index.html',valid=True,title=title,table_head=table_head,content=cur.fetchall())
if __name__ == '__main__':
    app.run(debug=True)
