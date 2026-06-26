import urllib.request
import random
url = 'http://www.baidu.com/s?wd=ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
request = urllib.request.Request(url=url, headers=headers)

proxies = {
    'http':'http://127.0.0.1:8080',
    'https':'https://127.0.0.1:8080'
}
# response = urllib.request.urlopen(request)
handler = urllib.request.ProxyHandler(proxies=random.choices(proxies))
print(handler)
opener = urllib.request.build_opener(handler)
response = opener.open(request)

content = response.read().decode('utf-8')
with open('daili.html', 'w', encoding='utf-8') as fp:
    fp.write(content)