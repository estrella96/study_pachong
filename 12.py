import requests
import json
from urllib import parse


baseurl="http://www.baidu.com/s?"
#dict格式
data={
    # girl 用户输入
    "kw":'girl'
}

# 构造一个请求头 请求头部应该至少包含传入的数据的长度
# request 要求dict
headers={
    'Content-Length':str(len(data))

}
rsp=requests.post(baseurl,data=data,headers=headers)

print(rsp.text)
# print(rsp.json())





