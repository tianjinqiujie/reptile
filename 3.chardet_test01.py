#-*- coding:utf-8 -*-
# 自动获取网页编码方式的方法
# pip install chardet 判断编码的模块

from urllib import request
import chardet
if __name__ == "__main__":
    response = request.urlopen("https://www.baidu.com")
    html = response.read()
    charset = chardet.detect(html)
    print(charset)
# {'language': '', 'confidence': 1.0, 'encoding': 'ascii'}