from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def open():
    q1=Options()
    q1.add_experimental_option('detach',True)
    service=Service('D:\\桌面\\chromedriver-win64\\chromedriver.exe')
    a1=webdriver.Chrome(service=service,options=q1)
    return a1

url = 'https://movie.douban.com/'
a1=open()
print(type(a1))
a1.get(url)
time.sleep(1)
a1.find_element(By.LINK_TEXT,'排行榜').click()
url1=a1.find_element(By.LINK_TEXT,'排行榜').get_attribute('href')
print(url1)
a1.get(url1)
a1.implicitly_wait(3)
# 十秒内找元素，找不到就报错，找到就继续立刻执行
a1.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/div/table[1]/tbody/tr/td[2]/div/a').click()
# 文件上传同样使用send_keys
time.sleep(1)


