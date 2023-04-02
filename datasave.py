import requests
import json
import mysql.connector

# 设置MySQL数据库连接参数
db_config = {
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'database': 'your_database'
}

# 设置Instagram API接口和个人访问令牌
url = "https://api.instagram.com/v1/users/self/follows/"
access_token = "your_access_token"

# 使用requests库发送HTTP请求并获取数据
response = requests.get(url, params={'access_token': access_token})
data = json.loads(response.text)

# 将数据存储在MySQL数据库中
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

for user in data['data']:
    id = user['id']
    username = user['username']
    full_name = user['full_name']
    profile_picture = user['profile_picture']
    cursor.execute("INSERT INTO follows (id, username, full_name, profile_picture) VALUES (%s, %s, %s, %s)", (id, username, full_name, profile_picture))

conn.commit()
cursor.close()
conn.close()
