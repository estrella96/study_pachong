from  urllib import request,parse
if __name__ == '__main__':
    url='http://www.baidu.com/s?'
    wd=input("Input your key word:")
    # 字典结构
    qs={
        "wd":wd
    }
    # 对url进行编码
    qs=parse.urlencode(qs)

    fullurl=url+qs
    print(fullurl)

    rsp=request.urlopen(fullurl)
    html=rsp.read()
    html=html.decode()
    print(html)

