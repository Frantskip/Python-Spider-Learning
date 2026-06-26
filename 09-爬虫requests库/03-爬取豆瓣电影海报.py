import requests
import urllib.request
from lxml import etree
import os
# os.mkdir('img')
base_url='https://movie.douban.com/top250'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'
}

from bs4 import BeautifulSoup
sum=0
if __name__ == '__main__':
    start_page = int(input('请输入开始的页数：'))
    end_page = int(input('请输入结束的页数：'))
    total=(end_page-start_page+1)*25
    for page in range(start_page,end_page+1):
        new_url = f'{base_url}?start={(page-1)*25}&filter='
        resp=requests.get(url=new_url,headers=headers)
        soup=BeautifulSoup(resp.text,'html.parser')
        msglist=soup.find_all('div',class_='pic')
        for elem in msglist:
            name=elem.find('img')['alt']
            src=elem.find('img')['src']
            urllib.request.urlretrieve(url=src,filename=f'img/{name}.jpg')
            sum+=1
            print(f'\r已下载{sum/total:.2%}',end='')

    print('下载完成')





