#-*- coding:utf-8 -*-
from urllib import request

if __name__ == "__main__":
    response = request.urlopen("https://www.baidu.com")
    html = response.read()
    # 返回信息进行解码
    html = html.decode('ascii')
    print(html)