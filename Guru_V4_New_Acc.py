from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
import time
import pandas as pd
import lxml

driver=webdriver.Chrome('C:\Python\chromedriver.exe')
driver.maximize_window()
driver.get("http://demo.guru99.com/V4/")
driver.implicitly_wait(10)

#User_id
User_id = driver.find_element_by_name("uid")
User_id.click()
User_id.send_keys("mngr346602")
time.sleep(1)

#password
password = driver.find_element_by_name("password")
password.click()
password.send_keys("YgupEze")
time.sleep(1)

#login
login = driver.find_element_by_name("btnLogin")
login.click()
time.sleep(1)

#New_Acc
New_Acc = driver.find_element_by_partial_link_text("New Account")
New_Acc.click()
time.sleep(1)

#Customer_id
Customer_id = driver.find_element_by_xpath("//input[@name='cusid']")
Customer_id.click()
Customer_id.send_keys(7)
time.sleep(1)

#Acc_type
Acc_type = driver.find_element_by_xpath("//select[@name='selaccount']")
Acc_type.click()
time.sleep(0.3)
Acc_type.click()
time.sleep(1)

#initial_deposit
initial_deposit = driver.find_element_by_xpath("//input[@name='inideposit']")
initial_deposit.click()
initial_deposit.send_keys(500)
time.sleep(1)

#submit_ok
submit_ok = driver.find_element_by_xpath("//input[@value='submit']")
submit_ok.click()
time.sleep(1)

#table_udaje
table_udaje = driver.find_element_by_xpath("//table[@id='account']").text
print(table_udaje)
time.sleep(3)

#continue_2
continue_2 = driver.find_element_by_xpath("//td[a='Continue']/a")
continue_2.click()
time.sleep(3)

driver.quit()
