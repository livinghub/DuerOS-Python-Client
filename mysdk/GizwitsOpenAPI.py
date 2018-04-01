# -*- coding: utf-8 -*-
' a Gizwits OpenAPI module '

__author__ = 'living'
__email__ = '707884308@qq.com'
__version__ = '0.0.1'

import requests
import time
import hashlib
import json


class GizwitsOpenAPI(object):
    def __init__(self, appid, usertoken):
        self.XGizwitsApplicationId = appid
        self.XGizwitsUsertoken = usertoken

    def GETAppUsers(self):
        url = "https://api.gizwits.com/app/users"
        headers = {"X-Gizwits-Application-Id": self.XGizwitsApplicationId,
                   "X-Gizwits-User-token": self.XGizwitsUsertoken}

        r = requests.get(url, headers=headers)
        print(r.json())

    def POSTAppBind_mac(self, product_key, product_secret, mac):
        XGizwitsTimestamp = int(time.time())  #获取时间戳
        s1 = product_secret + str(XGizwitsTimestamp)  #
        h1 = hashlib.md5()
        h1.update(s1.encode(encoding='utf-8'))
        XGizwitsSignature = h1.hexdigest() #签名，计算方法为 lower(md5(product_secret + timestamp)), timestamp 需与 X-Gizwits-Timestamp 一致

        url = "https://api.gizwits.com/app/bind_mac"
        headers = {"X-Gizwits-Timestamp": str(XGizwitsTimestamp),
                   "X-Gizwits-Signature": str(XGizwitsSignature),
                   "X-Gizwits-Application-Id": self.XGizwitsApplicationId,
                   "X-Gizwits-User-token": self.XGizwitsUsertoken
                   }
        payload = {"product_key": str(product_key),
                   "mac": str(mac),
                   "remark": "ture",
                   "dev_alias": "test",
                   "set_owner": 0
                   }
        r = requests.post(url, headers=headers, json=payload)
        json_response = r.content.decode() # 获取r的文本 就是一个json字符串
        json_dict = json.loads(json_response) #转换成字典
        did = json_dict['did']
        return did
        #print (did)
        #print(r.json())

    def POSTAppControl(self, did, payload):
        url = "https://api.gizwits.com/app/control/" + str(did)
        headers = {"X-Gizwits-Application-Id": self.XGizwitsApplicationId,
                   "X-Gizwits-User-token": self.XGizwitsUsertoken}
        '''payload = {
                    "attrs": {
                                 "light": 1,
                                "aaa": 60
                             }
                   }'''
        r = requests.post(url, headers=headers, json=payload)
        print(r.json())


''''
test = GizwitsOpenAPI("a56703ebcee94c5eb0325b3e684810f8", "6bb0c93fd2eb4d76bb141ea0b8977dfd")
did = test.POSTAppBind_mac("19ecdc9c991e407bb23610c98e461b6b", "5f01369401e24d90b6208a1a9b073da2", "ECFABC0CE2FA")
print(did)
payload = {
                    "attrs": {
                                "LED_Color": 0,
                                "LED_R": 0,
                                "LED_G": 0,
                                "LED_B": 0
                             }
                   }
test.POSTAppControl(did, payload)

'''''