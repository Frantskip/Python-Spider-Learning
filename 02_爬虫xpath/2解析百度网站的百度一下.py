import  urllib.request
from lxml import etree

url = 'https://www.baidu.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

tree = etree.HTML(content)
# xpath 返回值是列表
result = tree.xpath('//input[@id="su"]/@value')
print(result)