import urllib.request

url = 'https://weibo.cn/6451491586/info'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'Cookie':'_T_WM=42b84f163a325886b4a9cd1c86e3273d; SCF=AsbxUW8N1iqWF_ev--DKIf34ado8VcVf1qzV9I4y345tTyFe-HbO0egmBWFcQK21lKgfmQBogZ9d9QqTT-ZjGSk.; SUB=_2A25KqHmdDeRhGeFK41ES9SfPzDSIHXVpxPNVrDV6PUJbktAbLUTdkW1NQvUd41m6TpyCoPXDjjU9M5yipFbV9ysC; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWlvzpTVF-.A5v7JLwI_QzH5NHD95QNShn0e0-4e0MRWs4Dqcj6i--Ri-z7iKnpi--Xi-zRiKy8i--ciK.Ni-2Ni--Xi-iWi-iWi--Ri-2RiKn7i--ci-8hi-2Ei--Ni-8hiK.p; SSOLoginState=1739327949; ALF=1741919949'
}
request = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
with open('微博.html', 'w', encoding='utf-8') as fp:
    fp.write(content)
