#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3
from flask import Flask, render_template, request

DATABASE = 'database/data.db'
app = Flask(__name__)


def get_db():
    db = sqlite3.connect(DATABASE)
    return db


def valid_login(username, password):
    if username == u'root' and password == u'root':
        return True
    else:
        return False


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login_process():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            return render_template('index.html', valid=True)
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)


@app.route('/chiyao')
def chiyao():
    cur = get_db().cursor()
    cur.execute('SELECT id,name,chiyao,room FROM information')
    title = u'服药情况'
    table_head = [u'编号', u'姓名', u'是否已服药', u'房间号']
    return render_template('index.html', valid=True, title=title, table_head=table_head, content=cur.fetchall())


@app.route('/weisheng')
def weisheng():
    cur = get_db().cursor()
    cur.execute('SELECT id,name,weisheng,room FROM information')
    title = u'卫生情况'
    table_head = [u'编号', u'姓名', u'是否已打扫', u'房间号']
    return render_template('index.html', valid=True, title=title, table_head=table_head, content=cur.fetchall())


@app.route('/qiuzhu')
def qiuzhu():
    cur = get_db().cursor()
    cur.execute('SELECT id,name,qiuzhu,room FROM information')
    title = u'求助情况'
    table_head = [u'编号', u'姓名', u'是否需要帮助', u'房间号']
    return render_template('index.html', valid=True, title=title, table_head=table_head, content=cur.fetchall())


@app.route('/qichuang')
def qichuang():
    cur = get_db().cursor()
    cur.execute('SELECT id,name,qichuang,room FROM information')
    title = u'起床情况'
    table_head = [u'编号', u'姓名', u'是否已起床', u'房间号']
    return render_template('index.html', valid=True, title=title, table_head=table_head, content=cur.fetchall())


@app.route('/bingli')
def bingli():
    cur = get_db().cursor()
    cur.execute('SELECT disease.id,name,disease,year FROM information, disease WHERE information.id = disease.id')
    title = u'历史疾病'
    table_head = [u'编号', u'姓名', u'曾经得过的疾病', u'得病年份']
    return render_template('index.html', valid=True, title=title, table_head=table_head, content=cur.fetchall())


@app.route('/huodong')
def huodong():
    cur = get_db().cursor()
    cur.execute('SELECT id,name,huodong FROM information')
    title = u'现在的进行的文娱活动'
    table_head = [u'编号', u'姓名', u'现在的进行的文娱活动']
    return render_template('index.html', valid=True, title=title, table_head=table_head, content=cur.fetchall())

@app.route('/search', methods=['GET', 'POST'])
def search():
    key = request.form['search']
    cur = get_db().cursor()
    cur.execute("select * from information where name like '%" + key + "%'")
    title = u'搜索结果'
    table_head = [u'编号', u'姓名', u'房间号']
    return render_template('index.html', valid=True, title=title, table_head=table_head, content=cur.fetchall())

def valid_modiy(id, option):
    if id >=1 :
        print 'id:',id,'option:',option
        conn = get_db()
        cur=conn.cursor()
        cur.execute("update information SET chiyao = '"+ option + "' where id ="+ str(id))
        conn.commit()
        return True
    else:
        return False

@app.route('/modify_data',methods=['GET', 'POST'])
def modify_data():
    if request.method == 'POST':
        if valid_modiy(request.form['id'], request.form['option']):
            return render_template('index.html', valid=True)
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
