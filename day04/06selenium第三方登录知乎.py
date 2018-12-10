import time

from selenium import webdriver

#创建谷歌浏览器驱动,使用指定的驱动程序
driver = webdriver.Chrome(executable_path="/home/zhengyj/Downloads/chromedriver_linux64/chromedriver")

driver.get('https://www.zhihu.com')

#先点击登录
driver.find_element_by_xpath('//*[@class="SignContainer-switch"]/span').click()
time.sleep(1)

#第三方登录
#点击社交账号登录
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[5]/span[5]/button').click()
#然后点击QQ登录
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[2]/div[1]/form/div[5]/span[5]/span/button[3]').click()

time.sleep(20) #等待自己去登录qq账号或扫码

#最后刷新知乎页面
driver.refresh()

#登录后获取cookie
print(driver.get_cookies())


