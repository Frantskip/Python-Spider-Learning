import urllib.request
import urllib.parse


url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=20'

headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
request = urllib.request.Request(url = url ,headers= headers)
reponse = urllib.request.urlopen(request)

content =reponse.read().decode('utf-8')

# fp=open('豆瓣电影.json','w',encoding='utf-8')
# fp.write(content)
with open ('douban.json','w',encoding='utf-8') as fp:
    fp.write(content)
