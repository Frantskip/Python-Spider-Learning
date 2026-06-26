import requests

url='https://www.sogou.com/web'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
s=input('enter a word:')
params={
    'query':s
}
resp=requests.get(url=url,headers=headers,params=params)
content=resp.content.decode('utf-8')
print(content)
print(resp.status_code)
with open(s+'.html','w',encoding='utf-8') as fp:
    fp.write(content)
