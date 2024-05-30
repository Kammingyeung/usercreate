from flask import Flask, request, render_template
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create_user', methods=['POST'])
def create_user():
    # 从表单获取用户信息
    name = request.form['name']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    # Grafana 的详细信息
    grafana_url = "http://172.16.22.41:3000"  # 替换 <grafana_host> 为你的 Grafana 主机地址
    admin_user = "admin"  # 管理员用户名
    admin_password = "admin"  # 管理员密码

    # 构建新用户的数据
    new_user_data = {
        "name": name,
        "email": email,
        "login": username,
        "password": password
    }

    # 向 Grafana API 发送请求以创建新用户
    response = requests.post(
        f"{grafana_url}/api/admin/users",
        json=new_user_data,
        auth=HTTPBasicAuth(admin_user, admin_password)
    )

    # 根据响应结果返回信息
    if response.status_code == 200:
        return "New user created successfully."
    else:
        return f"Failed to create user. Status code: {response.status_code}, Response: {response.content}"


if __name__ == '__main__':
    app.run(debug=True)
