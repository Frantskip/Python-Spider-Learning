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

url = 'https://www.bilibili.com/'
a1=open()
a1.get(url)
a1.maximize_window()
time.sleep(3)

a1.find_element(By.LINK_TEXT,'番剧').click()
time.sleep(3)
a2=a1.window_handles
print(a2)
# a1.close()
a1.switch_to.window(a2[-1])
print(a1.current_url)
a1.find_element(By.CLASS_NAME,'nav-search-input').send_keys('鬼灭之刃')
a1.find_element(By.XPATH,'//*[@id="nav-searchform"]/div[2]').click()
a1.switch_to.window(a1.window_handles[-1])
a1.find_element(By.XPATH,'//*[@id="i_cecream"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/a/button').click()