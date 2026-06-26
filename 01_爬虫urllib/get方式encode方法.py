from urllib.request import *
import urllib.parse

# data ={
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾'
# }
# a =urllib.parse.urlencode(data)
# print(a)

base_url = 'https://www.baidu.com/s'
data={
    'wd':'周杰伦',
    'sex':'男',
    'location':'中国台湾省'
}
new_data=urllib.parse.urlencode(data)
url = base_url+'?'+new_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)
response = urlopen(request)
content = response.read().decode('utf-8')
print(content)