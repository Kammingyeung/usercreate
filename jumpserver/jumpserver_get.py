# Python 示例
# pip install requests drf-httpsig
import requests, datetime, json
from httpsig.requests_auth import HTTPSignatureAuth

def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth

def get_user_info(jms_url, auth):
    #获取所有用户信息
    # url = jms_url + '/api/v1/users/users/'
    #获取资产授权分组信息
    url = jms_url + '/api/v1/perms/asset-permissions/'
    gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
    headers = {
        'Accept': 'application/json',
        'X-JMS-ORG': '00000000-0000-0000-0000-000000000002',
        'Date': datetime.datetime.utcnow().strftime(gmt_form)
    }

    response = requests.get(url, auth=auth, headers=headers)
    print(json.loads(response.text))

if __name__ == '__main__':
    jms_url = 'http://172.16.22.41'
    KeyID = 'dc7cad72-27e4-4151-b78d-497e191ab5ba'
    SecretID = 'EAw4KR81v4hrhrvXliv8jF403ClG6MYREgNF'
    # jms_url = 'http://172.31.15.114:36180'
    # KeyID = '5102eddf-6072-459c-b48a-bdffef372453'
    # SecretID = '9dbf7dbb-4a3f-478d-a3e2-3ce6bb15df53'
    auth = get_auth(KeyID, SecretID)
    get_user_info(jms_url, auth)
