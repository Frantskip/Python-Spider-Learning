from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 设置 Chrome 浏览器二进制文件路径
path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'
chrome_options.binary_location = path

# 设置 ChromeDriver 路径
chromedriver_path = r'D:\桌面\chromedriver-win64\chromedriver.exe'
browser = webdriver.Chrome(options=chrome_options)

url = 'https://www.baidu.com'
browser.get(url)
browser.save_screenshot('baidu.png')
# 关闭浏览器
browser.quit()
