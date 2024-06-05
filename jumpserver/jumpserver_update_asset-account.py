import requests
import datetime
from httpsig.requests_auth import HTTPSignatureAuth

def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth

# 给资产授权规则添加指定账号
def add_account_to_permission(jms_url, auth, asset_permission_id, account_id_list):
    url = f'{jms_url}/api/v1/perms/asset-permissions/{asset_permission_id}/'
    gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
    headers = {
        'Accept': 'application/json',
        'X-JMS-ORG': '00000000-0000-0000-0000-000000000002',
        'Date': datetime.datetime.utcnow().strftime(gmt_form),
        'Content-Type': 'application/json'
    }

    # 要添加的账号ID列表
    accounts_data = {
        "name": 'test',
        "account": account_id_list
    }

    # 发送POST请求以添加账号到资产授权规则
    response = requests.put(url, auth=auth, headers=headers, json=accounts_data)
    return response  # 返回响应对象以便调用者处理

if __name__ == '__main__':
    jms_url = 'http://172.16.22.41'
    KeyID = 'dc7cad72-27e4-4151-b78d-497e191ab5ba'
    SecretID = 'EAw4KR81v4hrhrvXliv8jF403ClG6MYREgNF'
    # jms_url = 'http://172.31.15.114:36180'
    # KeyID = '5102eddf-6072-459c-b48a-bdffef372453'
    # SecretID = '9dbf7dbb-4a3f-478d-a3e2-3ce6bb15df53'
    auth = get_auth(KeyID, SecretID)

    # 资产授权分组的ID和要添加的账号ID列表
    asset_permission_id = '2fb84b75-0cf8-4580-87ee-d5e4c2cde4ea'  # 替换为实际的资产授权分组ID
    # 替换为实际的账号ID
    account_id_list = ['7639e3c0-b8d2-43f6-b60a-35b8891691c2']

    # 给资产授权规则添加指定账号
    response = add_account_to_permission(jms_url, auth, asset_permission_id, account_id_list)

    if response.status_code == 201:
        print("账号添加成功:", response.json())
    else:
        print("账号添加失败:", response.status_code, response.json())
