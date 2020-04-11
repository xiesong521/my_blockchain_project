#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
USERNAME = 'xiesong'
PASSWORD = '123456'
HOST = 'localhost'
PORT = 3306
DATABASE = 'python_admin'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8mb4'.format(username=USERNAME,password=PASSWORD,host=HOST,port=PORT,db=DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS =False
secret_key = "123456"