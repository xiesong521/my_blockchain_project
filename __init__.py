#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
#初始化参数
from flask import Flask
import configs
from extension import db
from views.user import user_page

app = Flask('my_blockchain_project')
app.config['SQLALCHEMY_DATABASE_URI']  = configs.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = configs.SQLALCHEMY_TRACK_MODIFICATIONS
app.secret_key = configs.secret_key

#初始化app
db.init_app(app)

#绑定蓝图
app.register_blueprint(user_page)
