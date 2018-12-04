# 有道翻译
from urllib import request,parse
import hashlib
import random
import time
import json

#定义md5加密函数
def getMD5(value):
    aa = hashlib.md5()
    aa.update(bytes(value,encoding="utf-8"))
    sign = aa.hexdigest()
    return sign

#定义请求函数
def fanyi(content):
    base_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    #对salt和sign进行js解析
    i = int(time.time() * 1000) + random.randint(0, 10)
    value ="fanyideskweb" + content + str(i) + "p09@Bn{h02_BIEe]$P^nG"
    data = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': i,
        'sign': getMD5(value),
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTIME',
        'typoResult': 'false',
    }
    # 使用urlencode方法转换标准格式
    data = parse.urlencode(data).encode('utf-8')
    headers = {
        'Accept': 'application / json, text / javascript, * / *; q = 0.01',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Connection': 'keep - alive',
        'Content - Type': 'application / x - www - form - urlencoded;charset = UTF - 8',
        'X - Requested - With': 'XMLHttpRequest',
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        'Content-Length': len(data),
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=168162067@218.241.251.155; OUTFOX_SEARCH_USER_ID_NCOO=2121343110.2274957; fanyi-ad-id=41685; fanyi-ad-closed=1; JSESSIONID=aaacmpXxOWbOKdy_3IIjw; ___rl__test__cookies=1522238432888'
    }
    res = request.Request(base_url,data=data,headers=headers,method='POST')
    #传递Request对象和转换完格式的数据
    response = request.urlopen(res)
    #读取信息并解码
    html = response.read().decode('utf-8')
    dict_data = json.loads(html)
    # print(dict_data)
    if dict_data.get("smartResult"):
        dic_data = dict_data.get("smartResult")
        di_data = dic_data.get("entries")
        # print(di_data)
        for data in di_data:
            if data != '\n':
                print(data)
    else:
        di_data = ''
        dic_data = dict_data.get('translateResult')
        # print(dic_data)
        for data in dic_data[0]:
            di_data += data.get('tgt')
        print(di_data)

if __name__ == '__main__':
    while True:
        content = input("请输入您需要翻译的内容（q 退出）:")
        if content == "q":
            break
        fanyi(content)   