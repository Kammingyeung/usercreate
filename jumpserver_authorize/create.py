from flask import Flask, request, jsonify
import requests
from httpsig.requests_auth import HTTPSignatureAuth
import json

app = Flask(__name__)

# Jumpserver的API基础URL
JUMPSERVER_BASE_URL = "http://172.16.22.41"
# Jumpserver API 身份验证信息
KeyID = 'a3243d76-7d4f-40a7-9415-4e0be3e63778'
SecretID = 'B2PeB2848yJb92AdMSoyxLfPbWeZRWE8a1mG'

def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth

@app.route('/authorize_root', methods=['POST'])
def authorize_root():
    # 获取前端发送的数据
    data = request.json
    authorizer_name = data['authorizer']
    ip_address = data['ipAddress']
    start_time = data['authorizationStartTime']
    end_time = data['authorizationEndTime']

    # 创建签名认证对象
    auth = get_auth(KeyID, SecretID)

    # 获取用户ID
    user_response = requests.get(
        f"{JUMPSERVER_BASE_URL}/api/v1/users/users/",
        auth=auth,
        params={"name": authorizer_name}
    )
    user_id = user_response.json()[0]['id']

    # 获取资产ID
    asset_response = requests.get(
        f"{JUMPSERVER_BASE_URL}/api/v1/assets/assets/",
        auth=auth,
        params={"ip": ip_address}
    )
    asset_ids = [asset['id'] for asset in asset_response.json()]

    # 创建资产授权规则
    permission_name = f"root临时分组{authorizer_name}"
    permission_data = {
        "name": permission_name,
        "user": user_id,
        "assets": asset_ids,
        "system_user": "root",
        "date_start": start_time,
        "date_end": end_time
    }
    permission_response = requests.post(
        f"{JUMPSERVER_BASE_URL}/api/v1/perms/asset-permissions/",
        auth=auth,
        json=permission_data
    )

    return jsonify(permission_response.json()), permission_response.status_code

@app.route('/authorize_user', methods=['POST'])
def authorize_user():
    # 获取前端发送的数据
    data = request.json
    asset_permission_id = data['assetPermissionId']
    asset_id_list = data['assetIdList']  # 前端需要提供资产ID列表

    # 创建签名认证对象
    auth = get_auth(KeyID, SecretID)

    # 更新资产授权规则
    assets_data = {
        "assets": asset_id_list
    }
    permission_response = requests.patch(  # 注意这里可能是PATCH或者是POST，根据Jumpserver的API来
        f"{JUMPSERVER_BASE_URL}/api/v1/perms/asset-permissions/{asset_permission_id}/",
        auth=auth,
        json=assets_data
    )

    return jsonify(permission_response.json()), permission_response.status_code

if __name__ == '__main__':
    app.run(debug=True)
