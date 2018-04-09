from urllib import request
from http import cookiejar

if __name__ == "__main__":
    # 设置保存cookie的文件，同级目录下的cookie.txt
    filename = 'cookie.txt'
    # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    cookie = cookiejar.MozillaCookieJar(filename)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    handler = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(handler)
    # 此处的open方法打开网页
    response = opener.open('http://www.baidu.com')
    # 打印cookie信息
    for item in cookie:
        print('Name = %s' % item.name)
        print('Value = %s' % item.value)
    # 保存cookie到文件
    '''
    ignore_discard的意思是即使cookies将被丢弃也将它保存下来；
    ignore_expires的意思是如果在该文件中cookies已经存在，则覆盖原文件写入。
    '''
    cookie.save(ignore_discard=True, ignore_expires=True)