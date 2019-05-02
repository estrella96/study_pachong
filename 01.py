#请求一个网页内容并打印
from urllib import request

if __name__ == '__main__':
    url="http://www.baidu.com"
    #打开相应url并把页面作为返回
    rsp=request.urlopen(url)
    #read 返回byte流
    html=rsp.read()
    html=html.decode("utf-8")
    print(html)


