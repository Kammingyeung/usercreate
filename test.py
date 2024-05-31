import requests, datetime, json
from httpsig.requests_auth import HTTPSignatureAuth


def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date', 'content-type']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth


def create_user(jms_url, auth, user_data):
    url = jms_url + '/api/v1/users/users/'  # 确保这是创建用户的正确端点
    gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',  # 添加了Content-Type头部
        'X-JMS-ORG': '00000000-0000-0000-0000-000000000002',
        'Date': datetime.datetime.utcnow().strftime(gmt_form)
    }

    response = requests.post(url, auth=auth, headers=headers, data=json.dumps(user_data))
    print(response.text)  # 更直接地打印响应文本


if __name__ == '__main__':
    jms_url = 'http://172.16.22.41'
    KeyID = '74a76830-9601-4bb1-9669-7f84cd8eab4f'
    SecretID = '8bbnPuH5TGJbredhPfzNycmX772qf6rVJl45'
    auth = get_auth(KeyID, SecretID)

    # 用户数据，根据Jumpserver API的要求进行调整
    user_data = {
        "username": "new_user",
        "name": "New User",
        "email": "new_user@example.com",
        "password": "a_strong_password"
        # ... 其他必要的用户字段
    }

    create_user(jms_url, auth, user_data)
