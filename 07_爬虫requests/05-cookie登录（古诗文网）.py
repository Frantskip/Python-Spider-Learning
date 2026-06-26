import requests
from bs4 import BeautifulSoup
import urllib.request
url = 'https://www.gushiwen.cn/user/login.aspx?from=http://www.gushiwen.cn/user/collect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

reponse = requests.get(url=url, headers=headers)
content = reponse.text

soup = BeautifulSoup(content, 'lxml')
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')

code = soup.select('#imgCode')[0].attrs.get('src')
code_url = 'https://so.gushiwen.cn' + code
session = requests.session()
response_code = session.get(url=code_url)
content_code = response_code.content
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)

# urllib.request.urlretrieve(url=code_url, filename='code.jpg')
code_name = input('请输入验证码：')

url_post = 'https://www.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fwww.gushiwen.cn%2fuser%2fcollect.aspx'
data_post = {
    '__VIEWSTATE':viewstate,
    '__VIEWSTATEGENERATOR': viewstategenerator,
    'from': 'http://www.gushiwen.cn/user/collect.aspx',
    'email': '3194455437@qq.com',
    'pwd': '123456',
    'code': code_name,
    'denglu': '登录',
}

response_post  = session.post(url=url_post, data=data_post, headers=headers)
cotent_post = response_post.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(cotent_post)
