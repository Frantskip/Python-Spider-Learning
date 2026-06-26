import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/sug'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

data = {
    'kw':'spider'
}
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url,data=data,headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

import json
obj = json.loads(content)
print(obj)