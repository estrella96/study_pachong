# 爬取豆瓣电影数据
# ajax

from urllib import request,error
import json

url="https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=40&limit=20"

rsp=request.urlopen(url)
data=rsp.read().decode()
data=json.loads(data)
print(data)
