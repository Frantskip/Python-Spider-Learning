from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
path = "D:\\桌面\\chromedriver-win64\\chromedriver.exe"
service = Service(path)
browser = webdriver.Chrome(service=service)

url = 'https://www.baidu.com'
browser.get(url)
import time
time.sleep(2)

input = browser.find_element(By.ID,'kw')
input.send_keys('周杰伦')
time.sleep(2)

button = browser.find_element(By.ID,'su')
button.click()
time.sleep(2)

js_button = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_button)
time.sleep(2)

next = browser.find_element(By.XPATH,'//a[@class="n"]')
next.click()
time.sleep(2)
browser.back()
time.sleep(2)
browser.forward()
time.sleep(3)
browser.quit()
