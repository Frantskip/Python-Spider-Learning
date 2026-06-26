import urllib.request
from lxml import etree
url = 'https://www.autohome.com.cn/cars/brand-15-x-x-x-x-1.html'

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "max-age=0",
    "Cookie": "_ac=90dd0461022007e3.1739848414; cookieCityId=421000; sessionip=27.26.213.57; sessionid=9ED659F2-6AEB-4933-9016-53C4FFF592C6%7C%7C2025-02-18+11%3A13%3A34.606%7C%7Cwww.baidu.com; autoid=ca68640a9755d2eda305045b7f43fe81; sessionvid=B9E0DD13-D047-43AC-8732-4875C2386F54; area=421024; __ah_uuid_ng=c_9ED659F2-6AEB-4933-9016-53C4FFF592C6; pvidchain=6861421,6861421,104399,6865139; ahpvno=10; v_no=8; visit_info_ad=9ED659F2-6AEB-4933-9016-53C4FFF592C6||B9E0DD13-D047-43AC-8732-4875C2386F54||-1||-1||8; ref=www.baidu.com%7C0%7C0%7C0%7C2025-02-18+11%3A23%3A46.247%7C2025-02-18+11%3A13%3A34.606; ahrlid=1739848688859R6cYzMUC4q-1739849275817",
    "Referer": "https://sou.autohome.com.cn/",
    # "Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    # "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
with open ('carhome.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
tree = etree.HTML(content)
name_list = tree.xpath('//div[@data-selected="false"]//div//@title')
for name in name_list:
    print(name)

