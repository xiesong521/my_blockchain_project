#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong

    Licence:MIT

"""
from flask import Flask, render_template, url_for, request, redirect, flash, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = 'mysql+pymysql://xiesong:123456@localhost:3306/python_admin?charset=utf8mb4'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "123456"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))


    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/users')
def users():
    if session.get('user_id'):
        users = User.query.all()
        return render_template('index.html', users=users)
    else:
        return redirect('/')


@app.route('/')
@app.route('/login', methods=['GET', 'PoSt'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        name = request.form.get('name')
        pwd = request.form.get('password')

        user = User.query.filter(User.username == name).first()

        if user and user.password == pwd:
            session['user_id'] = user.id
            return redirect(url_for('users'))
        else:
            flash('登陆失败')
            return render_template('login.html')


