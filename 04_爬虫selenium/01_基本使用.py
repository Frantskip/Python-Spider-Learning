from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import  time

# 指定 ChromeDriver 的绝对路径
path = "D:\\桌面\\chromedriver-win64\\chromedriver.exe"
# 创建 Service 对象
service = Service(path)

# 创建 Chrome 浏览器实例
browser = webdriver.Chrome(service=service)

# 要访问的网页 URL
url = 'https://www.baidu.com'
# 打开网页
browser.get(url)
# 等待 10 秒
time.sleep(10)
# 关闭浏览器
browser.quit()