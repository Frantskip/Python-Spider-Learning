import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
def open():
    q1=Options()
    q1.add_experimental_option('detach',True)
    service=Service('D:\\桌面\\chromedriver-win64\\chromedriver.exe')
    a1=selenium.webdriver.Chrome(service=service,options=q1)
    return a1

a1=open()
url='https://www.bilibili.com/'
a1.get(url)

# 浏览器查找多个元素 : document.getELementsByClassName('value')
time.sleep(3)
fanju = a1.find_element(By.LINK_TEXT,'番剧')
fanju.click()
newurl=fanju.get_attribute('href')
print(newurl)
# href = fanju.get_attribute('href')
#
# a1.get(href)
# time.sleep(3)
# try:
#     a1.find_element(By.CLASS_NAME,'index-categary-head').click()
# except Exception as e:
#     print(e)
