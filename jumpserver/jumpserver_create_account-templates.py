import requests
import datetime
import json
from httpsig.requests_auth import HTTPSignatureAuth


def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth

#批量创建账号模版
def create_asset_permission(jms_url, auth, name, username,secret):
    url = jms_url + '/api/v1/accounts/account-templates/'
    gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
    headers = {
        'Accept': 'application/json',
        'X-JMS-ORG': '00000000-0000-0000-0000-000000000002',
        'Date': datetime.datetime.utcnow().strftime(gmt_form),
        'Content-Type': 'application/json'  # 添加Content-Type头部
    }

    permission_data = {
        "name": name,
        "username": username,
        "secret": secret
    }

    # 发送POST请求
    response = requests.post(url, auth=auth, headers=headers, json=permission_data)
    print(json.loads(response.text))


if __name__ == '__main__':
    # jms_url = 'http://172.16.22.41'
    # KeyID = 'dc7cad72-27e4-4151-b78d-497e191ab5ba'
    # SecretID = 'EAw4KR81v4hrhrvXliv8jF403ClG6MYREgNF'
    jms_url = 'http://172.31.15.114:36180'
    KeyID = '5102eddf-6072-459c-b48a-bdffef372453'
    SecretID = '9dbf7dbb-4a3f-478d-a3e2-3ce6bb15df53'
    auth = get_auth(KeyID, SecretID)

    # 创建资产授权的名称和用户 UUID 列表
    permissions_list = [
        ("tt1", "tt1","tt1"),
    ]

    # 循环创建资产授权
    for name, username,secret in permissions_list:
        create_asset_permission(jms_url, auth, name, username,secret)