# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
#输入你的学号信息
your_id=input("请输入你的学号：")
your_password=input("请输入你的密码：")
#设置无头模式
option=webdriver.ChromeOptions()
option.add_argument('headless')
#打开浏览器
browser=webdriver.Chrome(chrome_options=option)
browser.get(r'http://jxgl.hdu.edu.cn/default.aspx')

#输入学号
input_id=browser.find_element_by_id("un")
input_id.clear()
input_id.send_keys(your_id)
#输入密码
input_pd=browser.find_element_by_id("pd")
input_pd.clear()
input_pd.send_keys(your_password)
#登录
btn_login=browser.find_element_by_id("index_login_btn")
btn_login.click()

#调出评价界面
span=browser.find_element_by_xpath("//a[@href='#a']")
span.click()
a=browser.find_element_by_xpath("//a[text()='理论教学质量评价']")
a.click()
#切换进iframe页面
time.sleep(5)
browser.switch_to.frame(0)

#得到所有需要评价课程
all_a=browser.find_elements_by_xpath("//select")
course=Select(all_a[0]).options

#评价每一门课程，前两个选项评价为B（满意），其余评价为A（非常满意）
for i in range(len(course)):
    all_a=browser.find_elements_by_xpath("//select")
    for j in range(1,len(all_a)):
        Select(all_a[j]).select_by_value("A（非常满意）")
        browser.implicitly_wait(30)
    Select(all_a[1]).select_by_value("B（满意）")
    Select(all_a[2]).select_by_value("B（满意）")
    browser.find_element_by_xpath("//input[@id='Button1']").click()
    time.sleep(2)
    browser.switch_to_alert().accept()
    time.sleep(2)
#提交退出
browser.find_element_by_xpath("//input[@id='Button2']").click()
browser.switch_to_alert().accept()
print("恭喜！你已经评价完成且已提交")







