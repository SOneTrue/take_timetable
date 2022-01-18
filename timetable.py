from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://btgp.ru/zameny-v-raspisanii.html")
assert "Расписание занятий техникума и замены" in driver.title
elem = driver.find_element(By.LINK_TEXT, 'расписание')
assert "No results found." not in driver.page_source
driver.close()