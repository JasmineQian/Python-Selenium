import os
from selenium import webdriver

chromedriver = "C:\\Users\\jasqia\\PycharmProjects\\HelloWorld\\Tools\\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


driver.get("https://yijia.acxiom.com.cn/ikeaMemberZoneV2/index.action?store=481")

driver.switch_to_frame("frame1")
driver.find_element_by_class_name("btn-update-info ").click()


driver.find_element_by_id("name").click()
driver.find_element_by_id("name").clear()
driver.find_element_by_id("name").send_keys(u"钱金燕")
print("钱金燕")
driver.find_element_by_id("mobile").click()
driver.find_element_by_id("mobile").clear()
driver.find_element_by_id("mobile").send_keys("17721658628")
print("17721658628")
driver.find_element_by_link_text(u"搜索").click()
print("------------------------")
print("=========================")
print("------------------------")
driver.quit()


