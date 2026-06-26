import requests
import urllib.request
import urllib.parse

url='https://www.sogou.com/web'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
# s=input('enter a word:')
#
s='周杰伦'
params={
    'query':s
}
print(urllib.parse.urlencode(params))
print(url+'?'+urllib.parse.urlencode(params))
request = urllib.request.Request(url=url,headers=headers,data=urllib.parse.urlencode(params).encode('utf-8'))
# print(request.get_full_url())
resp=urllib.request.urlopen(request)
content=resp.read().decode('utf-8')
# print(content)
# content=resp.content.decode('utf-8')
# print(resp.status_code)
# with open(s+'.html','w',encoding='utf-8') as fp:
#     fp.write(content)
