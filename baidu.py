# Author Liaosw
#coding=utf-8
from selenium import webdriver
driver = webdriver.Chrome()
#driver.maximize_window()
driver.set_window_size(480,800)#移动端大小

#访问百度首页
first_url = "https://www.baidu.com/"
print("now asses %s" %(first_url))
driver.get(first_url)

#访问新闻页面
second_url = "http://news.baidu.com/"
print("now asses %s" %(second_url))
driver.get(second_url)

#后退到百度首页
print("back to %s"%(first_url))
driver.back()

#前进到新闻页面
print("forward to %s" %(second_url))
driver.forward()

#driver.find_element_by_id("kw").send_keys("Selenium2")
#driver.find_element_by_id("su").click()
driver.quit()
