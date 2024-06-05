import requests
import datetime
import json
from httpsig.requests_auth import HTTPSignatureAuth


def get_auth(KeyID, SecretID):
    signature_headers = ['(request-target)', 'accept', 'date']
    auth = HTTPSignatureAuth(key_id=KeyID, secret=SecretID, algorithm='hmac-sha256', headers=signature_headers)
    return auth

#批量获取资产授权分组的id
def get_asset_permission_group_ids(jms_url, auth, group_names):
    url = jms_url + '/api/v1/perms/asset-permissions/'
    gmt_form = '%a, %d %b %Y %H:%M:%S GMT'
    headers = {
        'Accept': 'application/json',
        'X-JMS-ORG': '00000000-0000-0000-0000-000000000002',
        'Date': datetime.datetime.utcnow().strftime(gmt_form)
    }

    response = requests.get(url, auth=auth, headers=headers)
    asset_permissions = json.loads(response.text)

    group_ids = []
    for group_name in group_names:
        # 在资产授权分组中搜索指定的名称
        group_id = next((item.get('id') for item in asset_permissions if item.get('name') == group_name), None)
        if group_id:
            print(group_id)    #只获取分组id

if __name__ == '__main__':
    # jms_url = 'http://172.16.22.41'
    # KeyID = 'dc7cad72-27e4-4151-b78d-497e191ab5ba'
    # SecretID = 'EAw4KR81v4hrhrvXliv8jF403ClG6MYREgNF'
    jms_url = 'http://172.31.15.114:36180'
    KeyID = '5102eddf-6072-459c-b48a-bdffef372453'
    SecretID = '9dbf7dbb-4a3f-478d-a3e2-3ce6bb15df53'
    group_names = [
        'Administrator',
'CJ-伍思琼',
'CJ-刘冰',
'CJ-刘屏辉',
'CJ-彭新光',
'CJ-曾日日',
'CJ-林洁鑫',
'imx-bandit',
'imx-chenjing',
'imx-fanjinxia',
'imx-fengshuwen',
'imx-henrydeng',
'imx-huangyongzhi',
'imx-kong',
'imx-licanfeng',
'imx-shuxin',
'imx-yangjinheng',
'MaDev-andox',
'MaDev-eeyoung',
'MaDev-huangxinghui',
'MaDev-Joe',
'MaDev-joyce',
'MaDev-Keson',
'MaDev-lawjunkit',
'MaDev-samchan',
'MaDev-yongjian',
'MaDev-yumin',
'MaDev-zack',
'QY-刘合森',
'QY-刘毅炉',
'QY-卢文君',
'QY-吴威',
'QY-吴文锐',
'QY-唐铭聪',
'QY-曾卓',
'QY-杨峰',
'QY-梁超健',
'QY-苏子杰',
'QY-苏文杰',
'QY-郑灿彬',
'QY-陈伟杰',
'QY-陈嘉豪',
'QY-马骏宏',
'QY-黎焕文',
'SY-余涛',
'SY-刘若民',
'SY-吴建叠',
'SY-唐忠明',
'SY-宋佳虹',
'SY-徐荣敏',
'SY-李文',
'SY-杨兆宁',
'SY-杨金明',
'SY-杨钦钊',
'SY-林霄',
'SY-梁柱斌',
'SY-汤臣锡',
'SY-王振',
'SY-秦勇',
'SY-胡力丰',
'SY-胡文祥',
'SY-詹俊',
'SY-许昌顺',
'SY-谈鸿辉',
'SY-赵海',
'SY-邓学军',
'SY-邓浩宗',
'SY-郑嘉豪',
'SY-黄智聪',
'SY-黄江宇',
'孙自帝',
'市场部-FanYang',
'雪兰莪-liuzhihu',
'雪兰莪-luxuedong',
'雪兰莪-wangshuqing'
    ]  # 替换为您要查询的资产授权分组名称列表
    auth = get_auth(KeyID, SecretID)
    get_asset_permission_group_ids(jms_url, auth, group_names)
