import re

from bs4 import BeautifulSoup

# https://blog.csdn.net/c406495762/article/details/71158264
if __name__ == '__main__':
    html = """
    <html>
    <head>
    <title>Jack_Cui</title>
    </head>
    <body>
    <p class="title" name="blog"><b>My Blog</b></p>
    <li><!--注释--></li>
    <a href="http://blog.csdn.net/c406495762/article/details/58716886" class="sister" id="link1">Python3网络爬虫(一)：利用urllib进行简单的网页抓取</a><br/>
    <a href="http://blog.csdn.net/c406495762/article/details/59095864" class="sister" id="link2">Python3网络爬虫(二)：利用urllib.urlopen发送数据</a><br/>
    <a href="http://blog.csdn.net/c406495762/article/details/59488464" class="sister" id="link3">Python3网络爬虫(三)：urllib.error异常</a><br/>
    </body>
    </html>
    """
    soup = BeautifulSoup(html, 'lxml')
    # soup = BeautifulSoup(open(test.html), 'lxml')
    # print(soup.prettify())
    print(soup.title)
    print(soup.head)
    print(soup.a)
    print(soup.p)
    print(soup.title.name)
    print(soup.a.attrs)
    print(soup.a['class'])
    print(soup.a.get('class'))
    print(soup.title.string)
    print(soup.li)
    print(soup.li.string)
    print(type(soup.li.string))
    print(soup.find_all('a'))
    for tag in soup.find_all(re.compile("^b")):
        print(tag.name)
    print(soup.find_all(['title', 'b']))
    for tag in soup.find_all(True):
        print(tag.name)
    print(soup.find_all(attrs={"class": "title"}))
    print(soup.find_all(text="Python3网络爬虫(三)：urllib.error异常"))
    print(soup.find_all("a", limit=2))
    print(soup.find_all(class_="title"))

