from datetime import time

import selenium.webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def open():
    q1=Options()
    q1.add_experimental_option('detach',True)
    service=Service('D:\\桌面\\chromedriver-win64\\chromedriver.exe')
    a1=selenium.webdriver.Chrome(service=service,options=q1)
    return a1
import time
a1=open()
a1.get('https://www.baidu.com/')
time.sleep(1)
a1.set_window_position(200,200)
a1.set_window_size(100,100)