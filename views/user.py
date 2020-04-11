#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
# !/user/bin/python3
# coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com

    Copyright:XieSong

    Licence:MIT

"""
from flask import Flask, render_template, url_for, request, redirect, flash, session,Blueprint
from git_repo.my_blockchain_project.models import User

# 定义user的蓝图
user_page = Blueprint('user_page',__name__)

#user相关的各种路由

#用户登陆成功
@user_page.route('/users')
def users():
    if session.get('user_id'):
        users = User.query.all()
        return render_template('user/index.html', users=users)
    else:
        return redirect('/')

#首次登录，提交表单后的操作
@user_page.route('/')
@user_page.route('/login', methods=['GET', 'PoSt'])
def login():
    if request.method == 'GET':
        return render_template('user/login.html')
    else:
        name = request.form.get('username')
        pwd = request.form.get('password')

        user = User.query.filter(User.username == name).first()

        if user and user.password == pwd:
            session['user_id'] = user.id
            return redirect(url_for('users'))
        elif user and user.password != pwd:
            flash('密码错误,请重新输入！')
            return render_template('user/login.html')
        else:
            flash('该用户不存在，请重新输入！')
            return render_template('user/login.html')

#注册界面
@user_page.route('/sign_up')
def sign_up():
    return render_template('user/sign_up.html')
