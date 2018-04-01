# -*- coding:UTF-8 -*-
import GizwitsOpenAPI
import jieba
import jieba.posseg as pseg

jieba.set_dictionary('/home/pi/DuerOS-Python-Client/mysdk/dict.txt.small.user')
jieba.load_userdict('/home/pi/DuerOS-Python-Client/mysdk/user_dict.txt')

site_dic = {u'大厅': 1, u'房间': 2, u'卧室': 2}
device_dic = {u'的灯': 1, u'空调': 2, u'风扇': 3, u'电视': 4, u'开关': 5, u'电脑': 6}
action_dic = {u'打开': 1, u'开一下': 1, u'开了': 1, u'关了': 0, u'关闭': 0, u'关': 0, u'关上': 0}


def LightC(lightflag):
    
    if 'did' in dir() == True:
        pass
    else:
        light = GizwitsOpenAPI.GizwitsOpenAPI("a56703ebcee94c5eb0325b3e684810f8", "6bb0c93fd2eb4d76bb141ea0b8977dfd")
        did = light.POSTAppBind_mac("19ecdc9c991e407bb23610c98e461b6b", "5f01369401e24d90b6208a1a9b073da2", "ECFABC0CE2FA")

    if lightflag == 1:
        payload = {
            "attrs": {
                "LED_Color": 0,
                "LED_R": 200,
                "LED_G": 200,
                "LED_B": 200
            }
        }
    else:
        payload = {
            "attrs": {
                "LED_Color": 0,
                "LED_R": 1,
                "LED_G": 1,
                "LED_B": 1
            }
        }
    light.POSTAppControl(did, payload)
    return 1

def UserCmdP(site, device, action):
    sflag = 0
    if site == 1:
        if device == 1:
            if action == 1:
                sflag= LightC(1)
            else:
                sflag= LightC(0)
        elif device==2:
            if action == 1:
                sflag= LightC(1)
            else:
                sflag= LightC(0)
        elif device == 3:
            if action == 1:
                sflag= LightC(1)
            else:
                sflag= LightC(0)
    elif site == 2:
        if device == 1:
            if action == 1:
                sflag= LightC(1)
            else:
                sflag= LightC(0)
        elif device==2:
            if action == 1:
                sflag= LightC(1)
            else:
                sflag= LightC(0)
        elif device == 3:
            if action == 1:
                sflag= LightC(1)
            else:
                sflag= LightC(0)
    return sflag


def TextIn(usertxt):
    site_num = 0
    device_num = 0
    action_num = 0
    sflag = 0
    
    words = pseg.cut(usertxt)
    for w in words:
        if w.flag == "site":
            site_num = site_dic[w.word]
        if w.flag == "device":
            device_num = device_dic[w.word]
        if w.flag == "action":
            action_num = action_dic[w.word]

    print(site_num, device_num, action_num)
    sflag= UserCmdP(site_num, device_num, action_num)
    return sflag
    

#print(TextIn("把大厅的灯关闭"))
#UserCmdP()
#print(w.word, w.flag)