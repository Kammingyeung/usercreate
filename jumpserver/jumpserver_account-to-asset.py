import requests
import datetime
from httpsig.requests_auth import HTTPSignatureAuth

def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth

# 将账号模板添加到多个资产
def add_account_template_to_asset(jms_url, auth, asset_id, account_data):
    url = f'{jms_url}/api/v1/accounts/accounts/'  # 请根据JumpServer实际API调整此URL
    gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
    headers = {
        'Accept': 'application/json',
        'X-JMS-ORG': '00000000-0000-0000-0000-000000000002',
        'Date': datetime.datetime.utcnow().strftime(gmt_form),
        'Content-Type': 'application/json'
    }

    results = {}
    for asset_id in asset_ids:
        # 更新资产ID
        account_data['asset'] = asset_id
        # 发送POST请求
        response = requests.post(url, auth=auth, headers=headers, json=account_data)
        # 存储每个资产的响应结果
        results[asset_id] = response
    return results


if __name__ == '__main__':
    jms_url = 'http://172.16.22.41'
    KeyID = 'dc7cad72-27e4-4151-b78d-497e191ab5ba'
    SecretID = 'EAw4KR81v4hrhrvXliv8jF403ClG6MYREgNF'
    auth = get_auth(KeyID, SecretID)

    # 多个资产ID列表
    asset_ids = ['9ec7bd28-68bd-4ca4-bff2-a22e58a723e1', 'fd9fd268-e1fb-4ef1-bc9d-4e66d4cbd453']  # 替换为实际的资产ID列表
    account_data = {
        # "name": "tt",
        "privileged": False,
        "secret_type": "password",
        "template": "8e145428-928e-4729-b79e-bf2efe0dabef",  # 使用通用的账号模板ID
        # "username": "tt"
    }

    # 将账号模板添加到多个资产
    responses = add_account_template_to_asset(jms_url, auth, asset_ids, account_data)

    for asset_id, response in responses.items():
        if response.status_code == 201:
            print(f"账号模板成功添加到资产 {asset_id}:", response.json())
        else:
            print(f"账号模板添加到资产 {asset_id} 失败:", response.status_code, response.json())