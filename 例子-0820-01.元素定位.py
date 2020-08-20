#coding=utf-8
#导入webdriver驱动
from selenium import webdriver
#告诉系统打开浏览器是chrome
br=webdriver.Chrome()
#浏览器中打开页面
br.get("https://www.baidu.com")

#1.id定位
# br.find_element_by_id("kw").send_keys("醉叮当")
#2.name定位
# br.find_element_by_name("wd").send_keys("特朗普")
#3.class定位
# br.find_element_by_class_name("s_ipt").send_keys("拜登！")
#4.tag定位
# br.find_element_by_tag_name("input").send_keys("aaa")
#5.link标签
# br.find_element_by_link_text("新闻").click()
#6.partial_link
# br.find_element_by_partial_link_text("闻").click()
#7.xpath定位
#页面中所有元素搜索属性id的值是kw的进行操作
# br.find_element_by_xpath("//*[@id='kw']").send_keys("奥巴马")
#8.css定位
#页面中搜索属性id的值是kw的进行操作
br.find_element_by_css_selector("#kw").send_keys("拉登")
