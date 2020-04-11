#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
from extension import db

class User(db.Model):
    # 定义表名
    __tablename__ = 'users'
    #定义字段
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    # 一对一 一个用户对应一个角色
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64),unique = True)
    # 关联关系 一个role角色可以对应多个users  一对多
    users = db.relationship('User',backref = 'role')
    def __repr__(self):
        return '<Role %r>' % self.name