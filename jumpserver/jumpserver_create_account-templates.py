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
        ("liubing", "liubing", "abhp4JtsR&p2F1r"),
        ("liupinghui", "liupinghui", "dc5^Eryd%0GMt@0"),
        ("pengxinguang", "pengxinguang", "JjBcFKPcHLY33B3"),
        ("zengriri", "zengriri", "jt9obeX&YOSZnkQ"),
        ("linjiexin", "linjiexin", "ecTw0HiSAKWr*^j"),
        ("bandit", "bandit", "Nbe^i&%%oa76eNw"),
        ("chenjing", "chenjing", "fyN!O$FW3w8yM&8"),
        ("fanjinxia", "fanjinxia", "#m@gjR1iBnh3G6t"),
        ("fengshuwen", "fengshuwen", "en4OrCi@jHcUmnW"),
        ("henrydeng", "henrydeng", "Nam@lJq!%q!WVi8"),
        ("huangyongzhi", "huangyongzhi", "7rdByUereiQQ80m"),
        ("kong", "kong", "RsBPwD!AKg^Nlv8"),
        ("licanfeng", "licanfeng", "UCqWU&jeBBClBeu"),
        ("shuxin", "shuxin", "PEs@LrjYr@j8X#x"),
        ("yangjinheng", "yangjinheng", "rMhv#!bN1ad%DzX"),
        ("andox", "andox", "GeI0Ke1arjOV@Hq"),
        ("eeyoung", "eeyoung", "j%aK0GHZQDj3GTc"),
        ("Joe", "Joe", "tm4V8e^CIgTvtRj"),
        ("joyce", "joyce", "a2ppd!M9j1kJ$F6"),
        ("Keson", "Keson", "!$jJ1N^baIlcWq%"),
        ("lawjunkit", "lawjunkit", "COWpTW&6qUGYgYJ"),
        ("samchan", "samchan", "l1E9GxZXZm4$%Om"),
        ("yongjian", "yongjian", "SfYiDBG&c853h1c"),
        ("yumin", "yumin", "FZOdB8P&0QhT@sG"),
        ("zack", "zack", "Ktf7XTcYdXnd0^%"),
        ("liuhesen", "liuhesen", "*C0vMhxMSBjHzvD"),
        ("liuyilu", "liuyilu", "nw!&u7AsSzvNix*"),
        ("luwenjun", "luwenjun", "rHsbtlBpS0CG$rv"),
        ("wuwei", "wuwei", "!6^Qv38yMxX1TFh"),
        ("wuwenrui", "wuwenrui", "PqaUIvUh%ugot$E"),
        ("tangmingcong", "tangmingcong", "YxuSbnzKiHsg&Eg"),
        ("zengzhuo", "zengzhuo", "P#iTSTak%!lBNqS"),
        ("happytree", "happytree", "8oKJyu1#zT&g%pj"),
        ("liangchaojian", "liangchaojian", "BKRE925^ZYL7J!I"),
        ("suzijie", "suzijie", "V8QfG8G^1CnP8RM"),
        ("suwenjie", "suwenjie", "EiFU2OU!w74do%p"),
        ("zhengcanbin", "zhengcanbin", "fmqSzz#Y78f!bPe"),
        ("chenweijie", "chenweijie", "NoDCUJP8fmdtN5D"),
        ("chenjiahao", "chenjiahao", "Hayo#FIpYOew1E@"),
        ("majunhong", "majunhong", "!JJrFLZq39Ej7FN"),
        ("lihuanwen", "lihuanwen", "dFw6^K#unBLVMY5"),
        ("yutao", "yutao", "7O*T4dmyZM&RtsB"),
        ("liuruomin", "liuruomin", "Alt!^$6zUsf@vHa"),
        ("wujiandie", "wujiandie", "r&ZtlQ6FjKq*SdT"),
        ("tangzhongming", "tangzhongming", "NM$9T^5Kh^qR49Z"),
        ("songjiahong", "songjiahong", "u7SYTu9gOL@hmIu"),
        ("xurongmin", "xurongmin", "rDwTZC%#qbax6!p"),
        ("liwen", "liwen", "L6IuTlua0qGa*r8"),
        ("yangzhaoning", "yangzhaoning", "LvR69mThtw37Pn7"),
        ("yangjinming", "yangjinming", "cx!Qfuo0j*^&eTR"),
        ("yangqinzhao", "yangqinzhao", "E*f5t*0gWOwNopN"),
        ("linxiao", "linxiao", "5unMAT#Ci6Hu3Yg"),
        ("liangzhubin", "liangzhubin", "5Ts7kVl^6@4QPPk"),
        ("tangchenxi", "tangchenxi", "r2O&8t!Ceh0MfNk"),
        ("charleswone", "charleswone", "PBG18^DEr%1ki&Q"),
        ("qinyong", "qinyong", "$Wp!WHp!*U%u0An"),
        ("hulifeng", "hulifeng", "lYN#YBz0&fEFGl3"),
        ("huwenxiang", "huwenxiang", "mSgW^ywpv4N9vKO"),
        ("zhanjun", "zhanjun", "Ev1Z@IJJdt94Fdm"),
        ("xuchangshun", "xuchangshun", "S#GnUUo7&6tVFl#"),
        ("tanhonghui", "tanhonghui", "a!5mSKVPfZV76hl"),
        ("zhaohai", "zhaohai", "u#caNOWv0dcg3Sm"),
        ("dengxuejun", "dengxuejun", "Q$tKW!Fg63fQw@o"),
        ("denghaozong", "denghaozong", "uyw*$92sv!DsTCo"),
        ("zhengjiahao", "zhengjiahao", "xnKa6kPUr9J9EBw"),
        ("huangzhicong", "huangzhicong", "82CH22z@^U48&@m"),
        ("huangjiangyu", "huangjiangyu", "0bUqBDY2RQ0X#8A"),
        ("sunzidi", "sunzidi", "g7bv4y6Cekm%B@U"),
        ("FanYang", "FanYang", "vERqjE!QMalX$zO"),
        ("liuzhihu", "liuzhihu", "x@6hBvW*LB@524Q"),
        ("luxuedong", "luxuedong", "d9^&#VuJVE3Dmbl"),
        ("wangshuqing", "wangshuqing", "U$HvacWU&w9JD%o"),
    ]

    # 循环创建资产授权
    for name, username,secret in permissions_list:
        create_asset_permission(jms_url, auth, name, username,secret)