# -*- coding: utf-8 -*-

import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
import time

browser=webdriver.Chrome()
browser.get(r'http://www.pqdtcn.com/basic')

#单击弹窗的ok
btn=browser.find_element_by_class_name("confirm")
browser.implicitly_wait(30)
btn.click()

#运行js，选择分类导航
js="navigate('3')"
browser.execute_script(js)

#定位点击C
c_btn=browser.find_element_by_xpath("//button[contains(text(),'C')]")
c_btn.click()

#定位两个information science和library science
info=browser.find_element_by_xpath("//li[contains(text(),'Information science')]")
libr=browser.find_element_by_xpath("//li[contains(text(),'Library science')]")

#运行information science和library science对应的js
js_info="searchThesisInfo(1,arguments[0])"
browser.execute_script(js_info,info)
browser.execute_script(js_info,libr)

#运行检索按钮
search="searchBySubject();"
browser.execute_script(search)
browser.implicitly_wait(30)

#每页显示50个
browser.find_element_by_id("searchPageSize").find_element_by_xpath("//option[@value='50']").click()

#存储网址编号
urllist=[]
#调到第*页
#inputpage=browser.find_element_by_xpath("//input[@min='1']")
#btnpage=browser.find_element_by_class_name("layui-laypage-btn")
for i in range(1,900):
        try:
            inputpage=browser.find_element_by_xpath("//input[@min='1']")
            btnpage=browser.find_element_by_class_name("layui-laypage-btn")
            browser.implicitly_wait(30)
            inputpage.clear()
            browser.implicitly_wait(30)
            inputpage.send_keys(i)
            time.sleep(1)
            browser.implicitly_wait(30)
            btnpage.click()
            time.sleep(2)
            browser.implicitly_wait(30)
            html=browser.page_source
            url=re.findall(r'href="/thesisDetails/(.*?)"',html,re.S|re.M)
            urllist.append(url)
            browser.implicitly_wait(30)
        except StaleElementReferenceException:
            time.sleep(4)
df=pd.DataFrame(urllist)
df.to_excel(r'C:\Users\asusl\Desktop\urllist.xlsx',index=False)



