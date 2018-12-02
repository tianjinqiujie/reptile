# -*- coding: UTF-8 -*-
from urllib import request

if __name__ == "__main__":
    req = request.Request("https://wwww.baidu.com/")
    response = request.urlopen(req)
    print("geturl打印信息：%s"%(response.geturl()))
    # geturl打印信息：http://www.baidu.com/
    print('**********************************************')
    print("info打印信息：%s"%(response.info()))
    #     info打印信息：Date: Sun, 02 Dec 2018 12:57:26 GMT
    #     Content-Type: text/html
    #     Transfer-Encoding: chunked
    #     Connection: Close
    #     Vary: Accept-Encoding
    #     Set-Cookie: BAIDUID=66E53BBBFA31A5BC4C09895C8FA94CB3:FG=1; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    #     Set-Cookie: BIDUPSID=66E53BBBFA31A5BC4C09895C8FA94CB3; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    #     Set-Cookie: PSTM=1543755446; expires=Thu, 31-Dec-37 23:55:55 GMT; max-age=2147483647; path=/; domain=.baidu.com
    #     Set-Cookie: delPer=0; path=/; domain=.baidu.com
    #     Set-Cookie: BDSVRTM=0; path=/
    #     Set-Cookie: BD_HOME=0; path=/
    #     Set-Cookie: H_PS_PSSID=1464_21096_27245; path=/; domain=.baidu.com
    #     P3P: CP=" OTI DSP COR IVA OUR IND COM "
    #     Cxy_all: baidu+76bb11472abc8d411324897ae9a1d8fa
    #     Cache-Control: private
    #     Expires: Sun, 02 Dec 2018 12:57:09 GMT
    #     Server: BWS/1.1
    #     X-UA-Compatible: IE=Edge,chrome=1
    #     BDPAGETYPE: 1
    #     BDQID: 0xc90aa4d70002af7a
    print('**********************************************')
    print("getcode打印信息：%s"%(response.getcode()))
    # getcode打印信息：200