from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
path = "D:\\桌面\\chromedriver-win64\\chromedriver.exe"
service = Service(path)

browser = webdriver.Chrome(service=service)
url = 'https://www.baidu.com'
browser.get(url)
input = browser.find_element(By.ID,'su')
print(input.get_attribute('class'))
print(input.tag_name)
a = browser.find_element(By.LINK_TEXT,'新闻')
print(a.text)