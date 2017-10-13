import json

import requests
from requests.auth import HTTPBasicAuth


def testget1():
    r = requests.get(url='http://ip.taobao.com')  # 最基本的GET请求
    print(r.status_code)  # 获取返回状态
    r = requests.get(url='http://dict.baidu.com/s', params={'wd': 'python'})  # 带参数的GET请求
    print(r.url)
    print(r.text)


def testpost1():
    r = requests.post('https://api.github.com/some/endpoint', data=json.dumps({'some': 'data'}))
    print(r.json())


def testheader1():
    data = {'some': 'data'}
    headers = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    r = requests.post('https://api.github.com/some/endpoint', data=data, headers=headers)
    print(r.text)


def testresponse1():
    URL = 'http://ip.taobao.com/service/getIpInfo.php'  # 淘宝IP地址库API
    try:
        r = requests.get(URL, params={'ip': '8.8.8.8'}, timeout=1)
        r.raise_for_status()  # 如果响应状态码不是 200，就主动抛出异常
    except requests.RequestException as e:
        print(e)
    else:
        result = r.json()
        print(type(result), result, sep='\n')


def testfile1():
    url = 'http://127.0.0.1:5000/upload'
    files = {'file': open('/home/lyb/sjzl.mpg', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)

    # 将字符串作为文件上传
    files = {'file': ('test.txt', b'Hello Requests.')}  # 必需显式的设置文件名
    r = requests.post(url, files=files)
    print(r.text)


def testauth1():
    r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
    # r = requests.get('https://httpbin.org/hidden-basic-auth/user/passwd', auth=('user', 'passwd'))    # 简写
    print(r.json())


def testcookies1():
    url = 'http://httpbin.org/cookies'
    r = requests.get(url)
    print(tuple(r.cookies))

    # 发送cookie
    cookies = {'testCookies_1': 'Hello_Python3', 'testCookies_2': 'Hello_Requests'}
    # 在Cookie Version 0中规定空格、方括号、圆括号、等于号、逗号、双引号、斜杠、问号、@，冒号，分号等特殊符号都不能作为Cookie的内容。
    r = requests.get(url, cookies=cookies)
    print(r.json())


def testsession1():
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate, compress',
               'Accept-Language': 'en-us;q=0.5,en;q=0.3',
               'Cache-Control': 'max-age=0',
               'Connection': 'keep-alive',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

    s = requests.Session()
    s.headers.update(headers)

    _URL = 'http://xxx.xxx.xxx.xxx/pro/hxc/prouser/login.htm'
    r = s.post(_URL, params={'data': '{"phone":"123","passwd":"123","imgvcode":"wnds"}'})
    dicjson = r.json()
    userId = dicjson['data']['id']

    _URL = 'http://xxx.xxx.xxx.xxx/pro/hxc/prowallclass/list.htm'
    r = s.post(_URL,
               params={'data': '{"where":{"wallLevel":"normal"},"order":{"id":"desc"},"pageIndex":1,"pageSize":5}'})
    print(r.text)
    r.text['data']

def testtimeout1():
    requests.get('http://github.com', timeout=0.001)

def testproxy1():
    #采集时为避免被封IP，经常会使用代理。requests也有相应的proxies属性。

    import requests

    proxies = {
        "http": "http://10.10.1.10:3128",
        "https": "http://10.10.1.10:1080",
    }

    requests.get("http://www.zhidaow.com", proxies=proxies)
    #如果代理需要账户和密码，则需这样：

    proxies = {
        "http": "http://user:pass@10.10.1.10:3128/",
    }

if __name__ == '__main__':
    testtimeout1()
