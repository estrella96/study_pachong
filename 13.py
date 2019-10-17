#正则结果match的使用

import re

# 以小括号为单位分成两个组
s=r'([a-z]+) ([a-z]+)'
pattern =re.compile(s,re.I) #re.I忽略大小写
m=pattern.match("Hello world wide web")

# group(0)返回匹配成功的整个子串第一个
s=m.group(0) #Hello world
print(s)
# span(0)返回匹配成功的整个子串跨度
a=m.span(0)#(0,11)
print(a)

# group(1)返回第一个小组匹配成功的字串
s=m.group(1)#'Hello'
print(s)
# span(1)返回匹配成功的第一个子串跨度
a=m.span(1)#(0,5)
print(a)

# group(2)返回第二个小组匹配成功的字串
s=m.group(2)
print(s)
# span(0)返回匹配成功的第一个子串跨度
a=m.span(2)
print(a)

# group()等于group(1),group(2)
s=m.group()
print(s)

'''
Hello world
(0, 11)
Hello
(0, 5)
world
(6, 11)
Hello world
'''

#search
s=r'\d+'
pattern=re.compile(s)
m=pattern.search('one123434teow34324nj43',20,40)
print(m.group())

#findall
m=pattern.findall('fdwe234 5464 dsdf 5645')
print(m)

m=pattern.finditer('fdwe234 5464 dsdf 5645')
print(type(m))
for i in m:
    print(i.group())
