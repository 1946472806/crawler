from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
#设置代理
chromeOptions.add_argument("--proxy-server=http://202.20.16.82:10152")
#创建谷歌浏览器驱动,使用指定的驱动程序
browser = webdriver.Chrome(chrome_options=chromeOptions,executable_path="/home/zhengyj/Downloads/chromedriver_linux64/chromedriver")
browser.get('https://blog.csdn.net/zwq912318834/article/details/78626739')

print(browser.page_source)
#退出
browser.quit()