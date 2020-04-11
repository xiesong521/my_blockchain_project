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
import configs


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']  = configs.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = configs.SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = configs.secret_key
db = SQLAlchemy(app)


class User(db.Model):
    # 定义表名
    __tablename__ = 'users'
    #定义字段
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64),unique = True)
    users = db.relationship('User',backref = 'role')
    def __repr__(self):
        return '<Role %r>' % self.name

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
        name = request.form.get('username')
        pwd = request.form.get('password')

        user = User.query.filter(User.username == name).first()

        if user and user.password == pwd:
            session['user_id'] = user.id
            return redirect(url_for('users'))
        elif user and user.password != pwd:
            flash('密码错误,请重新输入！')
            return render_template('login.html')
        else:
            flash('该用户不存在，请何查用户名！')
            return render_template('login.html')


@app.route('/sign_up')
def sign_up():
    return render_template('sign_up.html')
