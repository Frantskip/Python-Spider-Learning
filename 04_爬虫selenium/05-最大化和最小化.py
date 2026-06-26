from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def dakai():
    q1=Options()
    q1.add_argument('--no-sandbox')
    q1.add_experimental_option('detach',True)

    service=Service('D:\\桌面\\chromedriver-win64\\chromedriver.exe')
    a1=webdriver.Chrome(service=service,options=q1)
    return a1

import time
a1=dakai()
a1.get('https://www.baidu.com')
time.sleep(3)
a1.maximize_window()
time.sleep(1)
a1.minimize_window()