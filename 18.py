from lxml import etree

# 只能读取xml html文件中是xml格式内容
html= etree.parse("./17.html")
# rst=etree.tostring(html,pretty_print=True)
# print(rst)
rst=html.xpath('//book')
print(type(rst))
print(rst)
rst=html.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)
rst=rst[0]
print(rst.tag)
print(rst.text)