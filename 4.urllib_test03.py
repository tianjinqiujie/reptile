# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    req = request.Request("https://www.baidu.com/")
    response = request.urlopen(req) # url也可以是一个Request对象
    html = response.read()
    html = html.decode("ascii")
    geturl = response.geturl()  # url的字符串
    info = response.info()  # meta标记的元信息，包括一些服务器的信息
    getcode = response.getcode()    # HTTP的状态码，如果返回200表示请求成功
    print(html)
    print(geturl)
    print(info)
    print(getcode)
