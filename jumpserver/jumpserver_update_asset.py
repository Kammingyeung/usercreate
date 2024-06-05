import requests
import datetime
import json
from httpsig.requests_auth import HTTPSignatureAuth

def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth

# 更新资产到资产授权分组
def update_asset_to_permission(jms_url, auth, asset_permission_id, asset_id_list):
    # 确保URL以斜杠结尾
    url = f'{jms_url}/api/v1/perms/asset-permissions/{asset_permission_id}/'
    gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
    headers = {
        'Accept': 'application/json',
        'X-JMS-ORG': '00000000-0000-0000-0000-000000000002',
        'Date': datetime.datetime.utcnow().strftime(gmt_form),
        'Content-Type': 'application/json'
    }

    # 要更新的资产ID列表
    assets_data = {
        "name": "CJ-刘屏辉",
        "assets": asset_id_list
    }

    # 发送PUT请求
    response = requests.put(url, auth=auth, headers=headers, json=assets_data)
    return response  # 返回响应对象以便调用者处理

if __name__ == '__main__':
    # jms_url = 'http://172.16.22.41'
    # KeyID = 'dc7cad72-27e4-4151-b78d-497e191ab5ba'
    # SecretID = 'EAw4KR81v4hrhrvXliv8jF403ClG6MYREgNF'
    jms_url = 'http://172.31.15.114:36180'
    KeyID = '5102eddf-6072-459c-b48a-bdffef372453'
    SecretID = '9dbf7dbb-4a3f-478d-a3e2-3ce6bb15df53'
    auth = get_auth(KeyID, SecretID)

    # 资产授权分组的ID和要更新的资产ID列表
    asset_permission_id = 'a7b15ee2-b77c-4abe-9297-67982cf8f033'  # 替换为实际的资产授权分组ID
    # 替换为实际的资产ID
    asset_id_list = \
['9db419e3-e197-4010-9e13-23222b9d9e8c', 'ed7d60e4-5a6d-48a3-99c6-fa4f3db6be57', 'a928ea18-95ca-4e04-b710-0275de60295f', '66753abf-a947-496e-8da8-ecbbd2988af2', '28ef4ad7-06c0-43a6-ab6a-5a9a97075475', '0ba45bb3-68d1-48de-9fcb-e898026d506b', '15cd940c-b3b6-4321-8aec-452eb59a11d5', 'f4a806a0-550e-4745-b6f6-e12834fda029', '6dfe237b-5ad7-4a51-a9c5-9ec62dd75726', 'e1953bd1-2973-4556-8ab7-00057cabdb3e', '14d82f52-efc2-46e8-9863-e0b330a8556c', 'e5eeff88-2d5d-4afd-8233-cd7379a42dcc', '4ac3a623-9828-4324-a1f7-70f14d1c911b']

    # 更新资产到资产授权分组
    response = update_asset_to_permission(jms_url, auth, asset_permission_id, asset_id_list)

    if response.status_code == 200:
        print("资产更新成功:", response.json())
    else:
        print("资产更新失败:", response.json())
