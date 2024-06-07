import requests
import datetime
import json
from httpsig.requests_auth import HTTPSignatureAuth

# 定义 get_auth 函数
def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth

#获取某个用户授权的所有资产
def get_user_assets(jms_url, auth, user_id):
    url = f'{jms_url}/api/v1/perms/users/{user_id}/assets/'
    gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
    headers = {
        'Accept': 'application/json',
        'Date': datetime.datetime.utcnow().strftime(gmt_form),
        'Content-Type': 'application/json'
    }

    response = requests.get(url, auth=auth, headers=headers)
    if response.status_code == 200:
        assets = response.json()
        return assets
    else:
        print(f'Error: {response.status_code}')
        return None

if __name__ == '__main__':
    # jms_url = 'http://172.16.22.41'
    # KeyID = 'dc7cad72-27e4-4151-b78d-497e191ab5ba'
    # SecretID = 'EAw4KR81v4hrhrvXliv8jF403ClG6MYREgNF'
    jms_url = 'http://172.31.15.114:36180'
    KeyID = '5102eddf-6072-459c-b48a-bdffef372453'
    SecretID = '9dbf7dbb-4a3f-478d-a3e2-3ce6bb15df53'
    user_id = '395c9604-55e1-4402-b3ca-991146c6af62'  # 用户的UUID
    auth = get_auth(KeyID, SecretID)

    user_assets = get_user_assets(jms_url, auth, user_id)
    if user_assets is not None:
        # print(json.dumps(user_assets, indent=2))
        if user_assets is not None:
            asset_ids = [asset.get('id') for asset in user_assets]  # 使用列表推导式获取所有资产ID
            # # asset_ids = [asset.get('address') for asset in user_assets]  # 使用列表推导式获取所有资产IP地址
            print(asset_ids)  # 打印资产ID列表
            # for asset in user_assets:
            #     print(asset.get('address'))  # 直接打印每个资产的IP地址
