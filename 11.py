'''
有参数的get
返回结果
'''

import requests

url="http://www.baidu.com/s?"

kw={
    "wd":"白敬亭"
}
headers={
    "User-Agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.1"

}

rsp=requests.get(url,params=kw,headers=headers)
print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.status_code)