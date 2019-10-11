from urllib import request,error
from http import cookiejar

cookie=cookiejar.CookieJar()
cookie_handler=request.HTTPCookieProcessor(cookie)

http_handler=request.HTTPHandler()

https_handler= request.HTTPSHandler()

opener= request.build_opener(http_handler,https_handler,cookie_handler)

def login():
#     初次登录，用户名和密码

if __name__ == '__main__':