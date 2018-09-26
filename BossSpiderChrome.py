import os
from time import strftime, localtime
from selenium import webdriver

chromedriver = ".\Tools\chromedriver.exe"
url2 = "https://m.zhipin.com/weijd/v2/job/1665531fe50fa0ea1XJ90tq1GVo~"
url3="https://m.zhipin.com/weijd/v2/job/c31807a4e76cddb21Xd-2tS0EFU~"
url1 = "https://yijiauat.acxiom.com.cn/Kiosk_Coupon/coup/"
url4="https://m.zhipin.com/weijd/v2/job/018cf113ffaf15ac1XF42Ny9FFA~"
url="https://m.zhipin.com/weijd/v2/job/0b96886ea49af6e21nF72ti5EFc~"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
print("======标题是"+driver.title)
print("======URL是"+driver.current_url)
#注释 print("======页面元素是"+driver.page_source)
print(driver.get_window_size())
time =strftime('%Y%m%d%H%M%S',localtime())
'''print(time)注释'''
"""print(time)注释"""
print(time)
driver.get_screenshot_as_file(".\\ScreenShot\\file_"+time+".png")
print(driver.get_window_position())

print (driver.find_element_by_css_selector ("div.boss-message").text)
print(driver.find_element_by_css_selector("p.name").text +"   薪资水平： "+driver.find_element_by_css_selector("p.salary").text)


print (driver.find_element_by_class_name ("detail-text").text)

print ("------职位信息结束------------")
driver.quit ()
