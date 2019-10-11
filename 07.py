# 代理服务器
# html写到文件

from urllib import request,error

if __name__ == '__main__':
    url="http://www.baidu.com"

    proxy={'http':'120.77.45.130:80'}
    proxy_handler=request.ProxyHandler(proxy)
    opener=request.build_opener(proxy_handler)
    request.install_opener(opener)

    try:
        rsp = request.urlopen(url)
        html = rsp.read().decode()
        print(html)
        with open("rsp.html","w") as f:
            f.write(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
print("done...")
