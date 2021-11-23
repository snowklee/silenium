from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import getpass
import json

login = getpass.getpass('Введите логин: ')
password = getpass.getpass('Введите пароль: ')

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://nstu.ru/")

time.sleep(1)

btn_login = driver.find_element_by_css_selector("div.header__login>a")
btn_login.click()
time.sleep(1)

btn_kabinet = driver.find_element_by_xpath('//a[text() = "Кабинет обучающегося"]')
btn_kabinet.click()

time.sleep(1)

input_login = driver.find_element_by_name("callback_0")
input_password = driver.find_element_by_name("callback_1")

input_login.send_keys(login)
input_password.send_keys(password)

input_password.send_keys(Keys.RETURN)

time.sleep(2)

btn_info = driver.find_element_by_css_selector("#ctSubTreeID3+table")
btn_info.click()
time.sleep(2)

btn_result = driver.find_element_by_css_selector("#ctSubTreeID4>table+table>tbody>tr>td+td+td>a")
btn_result.click()
time.sleep(2)

table = driver.find_elements_by_css_selector("table.tdall:nth-child(1n+2)")

l = table[0]
t = l.find_elements_by_css_selector("tbody>.all_progress")
i = 1
j = 0
n = 0
td = []
subjects = []
for t1 in t:
    t1 = t1.find_element_by_css_selector("td+td").text
    td.insert(n, t1)
td.remove('')
for td1 in td:
    print(td1)

to_json = {'subjects': td}
with open('subjects.json', 'w') as f:
    json.dump(to_json, f)

time.sleep(5)
driver.close()