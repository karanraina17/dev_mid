from selenium import webdriver
from selenium.webdriver.common.keys import Keys

b = webdriver.Firefox("geckodriver")
b.get('https://www.seleniumhq.org/')

b.set_page_load_timeout(10)
element = b.find_element_by_id('u_0_t')
element.send_keys('my_first_name')

element2 = b.find_element_by_id('u_0_v')
element2.send_keys('my_last_name')

element3 = b.find_element_by_id('u_0_y')
element3.send_keys('my_phone_no')

element4 = b.find_element_by_id('u_0_7')
element4.click()
