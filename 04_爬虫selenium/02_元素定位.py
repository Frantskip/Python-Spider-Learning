from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
path = "D:\\桌面\\chromedriver-win64\\chromedriver.exe"
service = Service(path)

browser = webdriver.Chrome(service=service)

url = 'https://www.baidu.com'
browser.get(url)

# button = browser.find_element(By.ID,'su')
# print(button)

# button = browser.find_element(By.NAME,'wd')
# print(button)

# button = browser.find_elements(By.XPATH,'//input[@id="su"]')
# print(button)

button = browser.find_elements(By.CSS_SELECTOR,'#su')
print(button)
