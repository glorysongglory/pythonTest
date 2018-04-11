import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    list_url = []
    for num in range(1, 20):
        if num == 1:
            url = 'http://www.shuaia.net/index.html'
        else:
            url = 'http://www.shuaia.net/index_%d.html' % num
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
        }
        req = requests.get(url=url, headers=headers)
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')
        targets_url = bf.find_all(class_='item-img')

        for each in targets_url:
            list_url.append(each.img.get('alt') + '=' + each.get('href'))
    print(list_url)
