from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# 替换为你的 Grafana 和 Jumpserver 信息
grafana_url = 'http://your-grafana-instance.com/api/admin/users'
grafana_api_key = 'your_grafana_api_key'
jumpserver_url = 'http://your-jumpserver-instance.com/api/users/'
jumpserver_token = 'your_jumpserver_token'

@app.route('/create_accounts', methods=['POST'])
def create_accounts():
    account_data = request.json
    username = account_data['username']
    password = account_data['password']

    # 创建 Grafana 账号
    grafana_response = requests.post(grafana_url, headers={
        "Authorization": f"Bearer {grafana_api_key}",
        "Content-Type": "application/json"
    }, json={
        "name": username,
        "email": f"{username}@example.com",
        "login": username,
        "password": password
    })

    # 创建 Jumpserver 账号
    jumpserver_response = requests.post(jumpserver_url, headers={
        "Authorization": f"Bearer {jumpserver_token}",
        "Content-Type": "application/json"
    }, json={
        "username": username,
        "password": password,
        "name": username,
        "email": f"{username}@example.com"
    })

    if grafana_response.ok and jumpserver_response.ok:
        return jsonify(success=True, message="Accounts created successfully")
    else:
        errors = {
            "grafana_error": grafana_response.text,
            "jumpserver_error": jumpserver_response.text
        }
        return jsonify(success=False, message=errors), 400

if __name__ == '__main__':
    app.run(debug=True)
