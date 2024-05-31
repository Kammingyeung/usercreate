# Python 示例
# pip install requests drf-httpsig
import requests, datetime, json
from httpsig.requests_auth import HTTPSignatureAuth

def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth

def get_user_info(jms_url, auth):
    url = jms_url + '/api/v1/users/users/'
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
    KeyID = '74a76830-9601-4bb1-9669-7f84cd8eab4f'
    SecretID = '8bbnPuH5TGJbredhPfzNycmX772qf6rVJl45'
    auth = get_auth(KeyID, SecretID)
    get_user_info(jms_url, auth)
