#百度通用翻译API,不包含词典、tts语音合成等资源，如有相关需求请联系translate_api@baidu.com
# coding=utf-8

import http.client
import hashlib
import urllib
import random
import json







def baidu_trans_api(q = 'dread'):
    appid = '20180902000201888'  # 填写你的appid
    secretKey = 'dveMma2P96LBqJqQ6nar'  # 填写你的密钥
    httpClient = None
    myurl = '/api/trans/vip/translate'

    fromLang = 'auto'   #原文语种
    toLang = 'zh'   #译文语种
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
    salt) + '&sign=' + sign

    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)

        # print (result)

    except Exception as e:
        print (e)
    finally:
        if httpClient:
            httpClient.close()
    if "trans_result" in result:
        return result["trans_result"][0]["dst"]
    else:
        return "Invalid Access Limit"



if __name__ == '__main__':
     
    while 1:
        word_to_trans = input("Please enter English (will be translated into Chinese): ")

        dst = baidu_trans_api(q = word_to_trans)
        print("----------> :", dst)
