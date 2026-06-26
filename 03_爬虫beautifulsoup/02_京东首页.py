import urllib.request

url = 'https://www.jd.com'
request =  urllib.request.Request(url)
response = urllib.request.urlopen(request)
cotent = response.read().decode('utf-8')
print(cotent)