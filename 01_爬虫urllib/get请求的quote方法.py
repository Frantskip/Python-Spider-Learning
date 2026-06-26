import urllib.request
import urllib.parse


url = 'https://www.baidu.com/s?wd='

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
name = urllib.parse.quote('周杰伦')
print(name)

url = url + name
print(url)
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
