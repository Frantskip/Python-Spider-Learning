import requests
import urllib.request
import urllib.parse
url='https://fanyi.baidu.com/sug'
s=input('enter a word:')
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    # 'Cookie':'PSTM=1740747222; BAIDUID=C16DB6E08DB342C483247DC99CA2EA6C:FG=1; BIDUPSID=B155AF69668749693E8050320212854A; MAWEBCUID=web_gEYimYAJjAxInlSSGhMDWlKdMfqBYRcHOZIXJfKtljyxrFbuCk; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=C16DB6E08DB342C483247DC99CA2EA6C:FG=1; ZFY=p81eggdLvdsno1rfi8:B4czLw4M7JMgt4PSocl1og07A:C; H_WISE_SIDS=61027_62079_62169_62230_62136_62325_62336_62345_62330_62373_62421_62423_62427; H_PS_PSSID=61027_62079_62169_62230_62136_62325_62336_62345_62330_62369_62373_62421_62423_62427_62441_62474; BA_HECTOR=04818lak81240k0525810k8l2kn2t91jsodmj22; delPer=0; PSINO=3; BCLID=8440599183546052786; BCLID_BFESS=8440599183546052786; BDSFRCVID=n6DOJexroGWInN5JzXaPJg86tuweG7bTDYrEFIaoSHTVG9FVvqHuEG0Pts1-dEu-S2OOogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; BDSFRCVID_BFESS=n6DOJexroGWInN5JzXaPJg86tuweG7bTDYrEFIaoSHTVG9FVvqHuEG0Pts1-dEu-S2OOogKKLgOTHULF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tRAOoC_-tDvtHJrwMDTD-tFO5eT22-usaJcR2hcHMPoosU3VhxIhyRIR-J3ZK5kqbTTf0l05KfbUotoHQxrHhptn3bjxqx5pbj67Ll5TtUJMqIDzbMohqqJXXPnyKMniBIv9-pnGBpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHjQ3ja7P; H_BDCLCKID_SF_BFESS=tRAOoC_-tDvtHJrwMDTD-tFO5eT22-usaJcR2hcHMPoosU3VhxIhyRIR-J3ZK5kqbTTf0l05KfbUotoHQxrHhptn3bjxqx5pbj67Ll5TtUJMqIDzbMohqqJXXPnyKMniBIv9-pnGBpQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKu-n5jHjQ3ja7P; ab_sr=1.0.1_NDE1NmI2YTllYmZhYjVmMDIxNGVjMmY2ZWUxMzBhMTFiYTVlNmEzMWNkNTAxNzU0NDNkNTZhMjI0ODQ3N2U0NWUyN2ZlMDEzY2RhNjRjYWFiZTg2MjM4YWQyODVkMTlmNDU2MTFlMjU4ZDM5NDAyYzIxOWVkMzVkYzFlODdlNzlmOWUwOTNiNTI0OWZhOGJmYjMyOGIwYmZhYjRkNzI0ZQ==; RT="z=1&dm=baidu.com&si=fb016125-3f31-47f9-8e47-3eccddfdbecc&ss=m810g719&sl=8&tt=96j&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=825f"'
}
data={
    'kw':s
}

# 使用urllib.request.Request
# request=urllib.request.Request(url=url,headers=headers,data=urllib.parse.urlencode(data).encode('utf-8'))
# resp=urllib.request.urlopen(request)
# content=resp.read().decode('utf-8')

# 使用requests
resp=requests.post(url=url,headers=headers,data=data)
content=resp.content.decode('unicode_escape')

print(content)
print(type(content))
import json
obj=json.loads(content)

for elem in obj['data']:
    print(elem['k'],'-->',elem['v'])
import requests
