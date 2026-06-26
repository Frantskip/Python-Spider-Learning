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
a1.get('https://zs.whut.edu.cn/bkcx/bklqqk/')
a1.set_window_size(2000,10000)
a1.get_screenshot_as_file('2.png')