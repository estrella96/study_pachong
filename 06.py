from urllib import request,error

if __name__ == '__main__':
    url="http://www.baidu.com"

    try:

        headers={}
        headers['User-Agent']='Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.1'
        req=request.Request(url,headers=headers)
        # req=request.Request(url)
        # req.add_header("User-Agent","xx")
        rsp=request.urlopen(req)
        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
print("done...")
