import requests
url = 'http://fanyi.baidu.com/sug'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}
data = {
    'kw': 'eye'
}

response = requests.post(url=url, data=data, headers=headers)
content = response.text
# print(content)
import json
obj = json.loads(content)
print(obj)