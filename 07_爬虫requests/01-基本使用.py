import requests
url = 'https://www.baidu.com'
reponse = requests.get(url)
# reponse.encoding = 'utf-8'

# print(reponse.text)

# print(reponse.url)

#返回二进制数据
# print(reponse.content)

# print(reponse.status_code)

print(reponse.headers)