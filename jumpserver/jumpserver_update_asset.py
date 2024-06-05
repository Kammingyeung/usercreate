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
        "name": "雪兰莪-wangshuqing",
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
    asset_permission_id = 'e1e37f5a-f3aa-4640-bb0e-34540bb8aa65'  # 替换为实际的资产授权分组ID
    # 替换为实际的资产ID
    asset_id_list = \
['8967219b-88fd-49de-ad2a-b3358c4a1913', 'bbdaf4d8-e87d-4fe0-8a3e-ca100b6f9b44', '55ee5b37-0d81-432a-a0d1-f85f9bcb74c5', 'cffdb9d1-9f9f-437c-b8f0-3547d0d86179', '3e188894-c4b2-4479-9cb8-0be3ae88e7b2', '359ee87e-de9e-439f-940b-6c912d401835', 'b7e950e5-e666-43da-a76a-a1d875898342', '80c2d276-99c5-4fb2-b566-0a93f51f8c02', 'cdb2111c-9bdd-43fd-83e8-f7d0c2531b53', '8f31eabc-35e0-46f7-ac7f-51aeb82bab26', '8f1c02b6-ff10-4171-a7cc-c86b6e3ffe6f', '5da3dc36-0a00-464b-ac47-28381295d96c', 'c5f28d7e-835f-4fdf-8a61-3406fd0beae2', '404443f0-bfea-4654-a7af-b10735a9e528', 'bec58e03-4196-47d9-9cb4-a895fae74701', '93bd3189-358a-4af4-ab3b-417d6887a7f1', 'd6bfdfe5-19fb-45cb-8ff1-ca964d4fab65', '318f7369-383e-4e92-a574-4bd54555c19d', '585f96b8-dd98-47a4-8444-6aea0bc3ccb5', '417fd7bc-59c8-4d4b-8f9f-1df8bf0414f0', 'cbbb1a50-f7f2-4599-abd0-c382b92662c0', '79e23fbd-b634-4003-a2dc-13ed969685d2', '7a9c8f9f-f851-4e2e-8f00-25dd0c9f1d25', '0a754b17-ed7f-4cad-a98e-f4e60c54a497', 'd668cca1-7312-4860-9ee2-f94694f798cc', '96b720d4-f14b-422d-b329-fcf9986595bd', '0d0e5b74-d093-4e1d-9b82-117cabfa57cf', '9bbe86f0-1bcd-458f-970a-600e977ee951', 'bfcbba02-57f0-4ba1-a814-ff6f10772390', '1dd73285-7e9f-4c47-8dd2-ce84c904db0f', '8f754074-c76a-4750-9144-64d95e36a9e8', '657f6f35-aae9-4596-84de-8fd875356be9', 'f63986c3-7fc9-42a4-9f05-3250440deaa7', 'b83f0716-aa80-4929-a311-ab72f10ff937', '686c1733-8dc3-43ef-bbd5-9f38c2b79b79', '9d0443a2-9b4f-4199-abf0-0cce8ad3ee76']

    # 更新资产到资产授权分组
    response = update_asset_to_permission(jms_url, auth, asset_permission_id, asset_id_list)

    if response.status_code == 200:
        print("资产更新成功:", response.json())
    else:
        print("资产更新失败:", response.json())
