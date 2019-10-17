#爬虫
- 资料
    - python网络数据采集
    - 精通Python爬虫框架Scrapy 人民邮电出版社
    - [blog](http://blog.csdn.net/c406495762/article/details/72858983)
    - Scrapy 官方教程
- 特征
    - 按要求下载数据或内容
    - 自动在网络上流窜
- 步骤
    - 下载网页
    - 提取信息
    - 跳转到另外的网页上
- 模块
    - urllib
    - urllib3
    - httplib2
    - requests
    
# urllib
- 模块 
    - urllib.request:打开和读取urls 01.py request.py里面有文档
    - urllib.error:包含urllib.request产生的常见错误
    - urllib.parse:解析url的方法
    - urllib.robotparse:解析robots.txt文件
- 网页编码问题
    - chardet: 自动检测文件编码格式 但可能有误
- urlopen 返回对象 01.py
    - geturl 返回请求对象的url
    - info 请求返回对象的meta信息
    - getcode 返回的http code
- request.data 的使用 02.py
    - 访问网络的方法
        - get
            - 利用参数给服务器传递信息
            - 参数为dict 用parse编码
        - post 03.py
            - 一般向服务器传递参数使用
            - post自动加密
            - data参数
            - http的请求头可能需要更改
                - Content-Type: application/x-www.form-urlencode
                - Content-Length: 数据长度
            - urllib.parse.urlencode 将字符串转换成上面的
            - 设置请求信息 urlopen不好用
            - 使用request.Request 类 04.py
- urllib.error
    - URLError: 05.py
        - 没有网络连接
        - 服务器连接失败
        - 找不到指定服务器
        - 是OSError的子类
    - HTTPError: URLError的子类
    - 区别
        - HTTPError对应HTTP请求的返回码错误 错误码400以上
        - URLError一般是网络出现问题 包括url问题
- UserAgent
    - UserAgent
        用户代理 heads的一部分
        服务器通过UA判断访问者身份
    - 设置UA
        - heads
        - add_header
        - 06.py
    - 常见UA值
```
        Personal Computer:
            Chrome浏览器:
            Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36
            
            Safari浏览器:
            
            Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0.3 Safari/604.5.6
            
            Firefox浏览器:
            
            Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:58.0) Gecko/20100101 Firefox/58.0
            
            QQ浏览器:
            
            Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36 QQBrowser/4.3.4986.400
            
            Edge浏览器:
            
            Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/13.10586
            
            IE11:
            
            Mozilla/5.0 (Windows NT 6.3; Win64, x64; Trident/7.0; rv:11.0) like Gecko
            
            IE10:
            
            Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)
            
            IE9:
            
            Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)
            
            IE8:
            
            Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)
            
            IE7:
            
            Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)
            
        MOBILE:
            
            Safari浏览器
            
            Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.1
            
            Chrome浏览器
            
            Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) CriOS/64.0.3282.112 Mobile/15D100 Safari/604.1
            
            QQ内置浏览器:
            
            Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 QQ/7.5.0.407 V1_IPH_SQ_7.5.0_1_APP_A Pixel/750 Core/UIWebView Device/Apple(iPhone 7) NetType/WIFI QBWebViewType/1
            
            QQ浏览器:
            
            Mozilla/5.0 (iPhone 91; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 MQQBrowser/8.0.2 Mobile/15D100 Safari/8536.25 MttCustomUA/2 QBWebViewType/1 WKType/1
            
            UC浏览器
            
            Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/15D100 UCBrowser/11.8.8.1060 Mobile AliApp(TUnionSDK/0.1.20.2)
            
            WeChat内置浏览器
            
            Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 MicroMessenger/6.6.3 NetType/WIFI Language/zh_CN
            
            Baidu浏览器
            
            Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11. Mobile/15D100 Safari/600.1.4 baidubrowser/4.13.0.16 (Baidu; P2 11.2.6)
            
            Sougou浏览器
            
            Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 SogouMobileBrowser/5.11.10
            
            Weibo内置浏览器:
            
            Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 Weibo (iPhone9,1__weibo__8.2.0__iphone__os11.2.6)
```
- ProxyHandler处理：代理服务器
    - 使用代理IP
    - 获取代理服务器的地址
        - www.xicidaili.com
        - www.goubanjia.com
    - 代理用来隐藏真实访问，代理不允许频繁访问一个固定网站
    - 使用步骤 07.py
        - 设置代理地址
        - 创建ProxyHandler
        - 创建Opener
        - 安装Opener

- cookie & session
    - http协议的无记忆性 采用的一个补充协议
    - cookie是发给用户的一段信息 session是保存在服务器上对应的另一半信息
    - 区别
        - 存放位置
            cookie 客户端
            session 服务器 一般在内存或者数据库中
        - cookie不安全
        - session会保存在服务器上一定时间 会过期
        - 单个cookie保存数据不超过4k 很多浏览器限制一个站点最多保存20个
    - 使用cookie
        - 把cookie复制下来手动添加 "Cookie"放入header
        - http模块包含一些关于cookie的模块
            - CookieJar
                管理存储cookie 向http请求添加cookie
                cookie在内存中 CookieJar实例回收后cookie消失
            - FileCookieJar(filename, delayload=None, policy=None)
                使用文件管理cookie
            - MozillaCookieJar(filename, delayload=None, policy=None)
                创建与mocilla浏览器cookie.txt兼容的FileCookieJar实例
            - LwpCookieJar(filename, delayload=None, policy=None)
                创建与libwww-perl标准兼容的set-cookie3格式的FileCookieJar实例
        - 利用cookiejar访问 08.py
            - 打开登录页面自动通过用户名密码登录
            - 自动提取反馈回来的cookie
            - 利用提取的cookie登录隐私页面
- SSL
    - SSL证书是指遵守SSL安全套接层协议的服务器数字证书

- js加密

- ajax 09.py
    - 异步请求
    - 一定有url+请求方法+可能有数据
    - 一般用json格式

# Requests模块
- 继承了urllib所有特征
- 底层使用的是urllib3
- 开源地址: https://github.com/requests/requests
- 中文文档：http://docs.python-requests.org/zh_CN/latest/index.html
- 安装： conda install requests
- get请求 10.py
    - requests.get(url)
    - requests.request("get",url)
    - 可以带有headers和parmas参数
    - get 返回内容 11.py
- post请求 12.py
    - rsp=requests.post(url,data=data)
    - data,headers要求dict类型 不需要转码
- proxy 代理
    proxies={
    "http":"address of proxy"
    "https":"address of proxy"}
    
# 页面解析和数据提取
- 结构数据：先有结构，再谈数据
    - JSON文件
        转换成Python类型操作 json类
    - XML文件
        转换成Python类型xmltodict
        XPath
        CSS选择器
        正则
- 非结构数据：先有数据 再谈结构
    - 文本 电话号码 邮箱地址
        通常用正则表达式处理
    - HTML文件
        正则表达式 XPath CSS选择器
    
##正则表达式
- 一套规则 可以在字符串文本中进行搜查替换
- re基本使用流程
- match使用 13.py
- 正则常用方法
    - match：从开始位置开始查找 一次匹配
    - search：从任何位置开始查找 一次匹配
    - findall: 全部匹配 返回列表
    - finditer：全部匹配 返回迭代器
    - split：分割字符串 返回列表
    - sub：替换
- 匹配中文 14.py
    - 中文unicode编码范围[u4e00-u9fa5]
- 贪婪与非贪婪模式
    - 贪婪模式：在整个表达式匹配成功的前提下 尽可能多的匹配
    - 非贪婪：。。。。尽可能少的匹配
    - python默认贪婪模式

## XML  15.xml
- 可扩展的标记性语言 为了传输数据 W3school

## XPath
- XML Path Language XML中查找信息
- W3school
- XPath 开发工具 
    XMLQuire 
    Chrome: Xpath Helper
- 常用路径表达式 
    - nodename：节点的所有子节点
    - /: 从根节点开始选
    - //: 选取元素 不考虑元素的具体位置
    - .: 当前节点
    - ..: 父节点
    - @ ：
    - 例子
        - bookstore：选取所有子节点
        - /bookstore: 选取根元素
        - bookstore/book: 选取bookstore的所有为book的子元素
        - //book :选取book
        - //@lang:选取名称为lang的所有属性
- 谓语 Predicate
    - 查找某个特定节点  卸载方括号中
    - /bookstore/book[1]:选第一个book
    - /bookstore/book[last()]
    - /bookstore/book[position()<3]:前两个
    -/bookstore/book[@lang="cn"]
- 通配符
    - * : 任何元素节点
    - @*：匹配任何属性节点
    - node():匹配任何类型节点
- 选取多个路径
    - | 或者

## lxml 类
- python 的html/xml解析器
- http://lxml.de/index.html
- 功能
    1 解析html 16.py
    2 文件读取 17.html 18.py