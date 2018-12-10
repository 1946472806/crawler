import time

from selenium import webdriver

#创建谷歌浏览器驱动,使用指定的驱动程序
driver = webdriver.Chrome(executable_path="/home/zhengyj/Downloads/chromedriver_linux64/chromedriver")

driver.get('https://www.zhihu.com')

#先点击登录
driver.find_element_by_xpath('//*[@class="SignContainer-switch"]/span').click()
time.sleep(1)

#输入用户名
username = driver.find_element_by_name("username")
username.send_keys('18588403840')
time.sleep(1)

#输入密码
password = driver.find_element_by_name("password")
password.send_keys('Changeme_123')
time.sleep(8)

#登录
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/button').click()