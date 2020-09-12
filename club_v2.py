
import requests
from lxml import html
from bs4 import BeautifulSoup as bs








# if __name__ == '__main__':
#     pass
    # links = []  # 用來裝所有牛奶連結的list
    # url = "https://online.carrefour.com.tw/%E9%AE%AE%E4%B9%B3?parentSeName=%E5%86%B7%E5%87%8D%E5%86%B7%E8%97%8F%E9%A3%9F%E5%93%81"
    # for count in range(1, 6):
    #     payload = 'categoryId':366,'pageIndex':count,'orderBy':0,
    #     'listType':'list-type-vertical'
    #     r = requests.post(url, params=payload)
    #     content = r.text
    #     soup = BeautifulSoup(content, 'html.parser')
    #     for div in soup.find_all('div', class_= 'product_list_img'):
    #         for link in div.find_all('a', href = True):
    #             print(link['title'])  # 商品名稱
    #             completeURL = 'https: // online.carrefour.com.tw' + link['href']
    #             if completeURL not in links:
    #                 links.append(completeURL)  # 將連結加入list裡
    # print(links)

    # USEREMAIL = 'dushiun@example.com'
    # PASSWORD = 'jason870225'
    # LOGIN_URL = 'https://www.facebook.com/'
    # session_requests = requests.session()
    # result = session_requests.get(LOGIN_URL)
    # tree = html.fromstring(result.text)
    # authenticity_token = list(set(tree.xpath('//input[@name="csrfmiddlewaretoken"]/@value')))[0]
    # {
    #     "name":"Accept",
    #     "value":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    #     "name":"Accept-Encoding","value":"gzip, deflate, br",
    #     "name":"Accept-Language","value":"zh-TW,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    #     "name":"Connection","value":"keep-alive",
    #     "name":"Content-Length","value":"288",
    #     "name":"Content-Type","value":"application/x-www-form-urlencoded",
    #     "name":"Cookie","value":"fr=1dIXgCsvRTVDijUeC..BfXFVu.nf.AAA.0.0.BfXFXV.AWVauY64; sb=blVcX8q2ev1R7z7MDs-qIUPv; wd=1295x576; datr=blVcX97s_UXzUf7mmZh7SHz_",
    #     "name":"DNT","value":"1",
    #     "name":"Host","value":"www.facebook.com",
    #     "name":"Origin","value":"https://www.facebook.com",
    #     "name":"Referer","value":"https://www.facebook.com/",
    #     "name":"TE","value":"Trailers",
    #     "name":"Upgrade-Insecure-Requests",
    #     "value":"1",
    #     "name":"User-Agent","value":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0"
    # }

USEREMAIL = 'yourname@example.com'
PASSWORD = '*******'

LOGIN_URL = 'https://anewstip.com/accounts/login/'

def main():
    for i in range(1, 11):
        URL = 'https://anewstip.com/search/journalists/?q=privacy&page=' + str(i)
        session_requests = requests.session()

        result = session_requests.get(LOGIN_URL)
        tree = html.fromstring(result.text)
        authenticity_token = list(set(tree.xpath('//input[@name="csrfmiddlewaretoken"]/@value')))[0]

        headers = {
            'Connection': 'keep-alive',
            'Content-Length': '103',
            'Cache-Control': 'max-age=0',
            'Origin': 'https://anewstip.com',
            'Upgrade-Insecure-Requests': '1',
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Referer': LOGIN_URL,
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cookie': '_ga=GA1.2.218269643.1513734952; _gid=GA1.2.1405785245.1513907212; csrftoken='+authenticity_token+'; sessionid=yvb8vq6m4katwmz76d0cnjubd29pdrdb; _gat=1'
        }

        payload = {
            'email': USEREMAIL,
            'password': PASSWORD,
            'csrfmiddlewaretoken': authenticity_token
        }

        result = session_requests.post(LOGIN_URL, data = payload, headers = headers)

        result = session_requests.get(URL, headers = dict(referer = URL))
        soup = bs(result.text, 'html.parser')

        for link in soup.select('.info-name a'):
            print('https://anewstip.com/'+link.get('href'))

if __name__ == '__main__':
    main()

    


















