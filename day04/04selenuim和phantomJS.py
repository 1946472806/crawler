from selenium import webdriver

#创建谷歌浏览器驱动,使用指定的驱动程序
driver = webdriver.Chrome(executable_path="/home/zhengyj/Downloads/chromedriver_linux64/chromedriver")

#get():打开百度页面
driver.get('http://baidu.com')

#page_source:获取网页源码
# print(driver.page_source)

#关闭
# driver.close() #(只关闭当前网页)
# driver.quit() #关闭所有窗口

#按照节点查找
kw_ipt = driver.find_element_by_xpath('//*[@id="kw"]')
# print(kw_ipt)
#给节点设置内容
kw_ipt.send_keys('陈羽凡')

#截屏
driver.save_screenshot('baidu.png')

