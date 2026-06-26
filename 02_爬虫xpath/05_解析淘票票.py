import urllib.request

url = 'http://dianying.taobao.com/cityAction.json?city=110100&_ksTS=1739367369125_19&jsoncallback=jsonp20&action=cityAction&n_s=new&event_submit_doLocate=true'
headers = {
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    # "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "t=7458eb548c734d9e3371481cd13d37b8; cookie2=1bc21bb9865ff94e6ddb77cf30c7cd0a; v=0; _tb_token_=eebe53e7e353d; cna=+o4zIEDFqFUCARsa1TnAPi1a; xlly_s=1; tb_city=110100; tb_cityName=\"sbG+qQ==\"; isg=BDMz5E3xUHbVBhyidfuJurbEwjddaMcqOwsP7uXRX9J95FKGbTpqesE3nhQK7x8i",
    "Referer": "https://dianying.taobao.com/cinemaList.htm?spm=a1z21.3046609.header.5.765c112aveAzA0&n_s=new",
    "Sec-Ch-Ua": "\"Chromium\";v=\"121\", \"Not A(Brand\";v=\"99\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest"
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
