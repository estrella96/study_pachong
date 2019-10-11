# 模拟post请求
# 请求地址http://fanyi.baidu.com/sug
# 网页Network-All-Headers FormData的值是kw:girl
# 返回json格式内容
'''
流程：
    1 利用data构造内容 然后urlopen打开
    2 返回一个json格式的结果
    3 结果应该是girl的释义
'''
from urllib import request,parse
import json

baseurl="http://fanyi.baidu.com/sug"

#dict格式
data={
    # girl 用户输入
    "kw":'girl'
}
data=parse.urlencode(data).encode('utf-8')
# 构造一个请求头 请求头部应该至少包含传入的数据的长度
# request 要求dict
headers={
    'Content-Length':len(data)

}
rsp=request.urlopen(baseurl,data=data)

json_data=rsp.read().decode('utf-8')
print(json_data)

# 转换成字典格式
json_data=json.loads(json_data)
print(json_data)

for item in json_data['data']:
    print(item['k'],"---",item['v'])





