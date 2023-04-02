import mysql.connector
from instapy import InstaPy

# 设置MySQL数据库连接参数
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

# 设置Instagram账号和密码
username = 'your_instagram_username'
password = 'your_instagram_password'

# 创建InstaPy对象并登录
session = InstaPy(username=username, password=password)
session.login()

# 从MySQL数据库中获取已存储的用户信息
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()
cursor.execute("SELECT username FROM follows")
users = [user[0] for user in cursor.fetchall()]

# 在Instagram中关注这些用户
for user in users:
    session.follow(user)

# 关闭InstaPy对象和数据库连接
session.end()
cursor.close()
conn.close()
