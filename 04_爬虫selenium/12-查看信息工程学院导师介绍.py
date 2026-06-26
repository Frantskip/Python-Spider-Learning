from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

service=Service('D:\\桌面\\chromedriver-win64\\chromedriver.exe')
a1=webdriver.Chrome(service=service)
a1.implicitly_wait(10)
a1.get('https://www.baidu.com/')
a1.find_element(By.ID,'kw').send_keys('武汉理工大学信息工程学院')

a1.find_element(By.ID,'su').click()
time.sleep(3)
try:
    a1.find_element(By.XPATH,'//*[@id="1"]/div/div/div/div[1]/div/h3/a/div/div/p/span/span/span').click()
    #//*[@id="1"]/div/div/div/div[1]/div/h3/a/div/div/p/span/span/span

    time.sleep(2)
    a1.switch_to.window(a1.window_handles[-1])


    teacher_link = a1.find_element(By.LINK_TEXT, '研究生培养')  # 使用精确文本定位
    print("导师页面地址:", teacher_link.get_attribute('href'))
    teacher_link.click()

    # 切换到新窗口
    a1.switch_to.window(a1.window_handles[-1])
    time.sleep(2)


    a1.find_element(By.XPATH,'/html/body/div[2]/div[1]/ul/li[6]/a').click()

    jds_url = a1.find_element(By.LINK_TEXT,'姜德生').get_attribute('href')
    print("导师介绍页面地址:", jds_url)
    time.sleep(2)
    a1.find_element(By.LINK_TEXT,'姜德生').click()
except Exception as e:
    print("完整错误信息:", repr(e))
    print(e)

print(a1.current_url)

time.sleep(10)
a1.quit()



