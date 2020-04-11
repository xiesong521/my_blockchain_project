#!/user/bin/python3
#coding:utf-8
"""
    Author:XieSong
    Email:18406508513@163.com
    
    Copyright:XieSong
    Licence:MIT

"""
from app import db
from app import User,Role
#删除表
# db.drop_all()
#创建表
# db.create_all()
admin_role = Role(name = 'Admin')
mod_role = Role(name = 'Moderator')
user_role = Role(name = 'User')
user1 = User(username = 'xiesong',email = '22@163.com',password='123456',role=admin_role)
user2 = User(username = 'chaoren',email = '33@163.com',password='123456',role=mod_role)
user3 = User(username = 'liguo',email = '23@163.com',password='123456',role=user_role)

# db.session.add(admin_role)
# db.session.add(mod_role)
# db.session.add(user_role)
# db.session.add(user1)
# db.session.add(user2)
# db.session.add(user3)
# #
# db.session.commit()


# get 主键
admin_role = Role.query.get(23)
print(admin_role)
admin_user=admin_role.role.filter().all()
print(admin_user)