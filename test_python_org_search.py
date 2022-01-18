from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()
    driver.get('https://btgp.ru/zameny-v-raspisanii.html')
    assert "Расписание занятий техникума и замены" in driver.title
    # btn = driver.find_element(By.CLASS_NAME, 'page-header')
    f ='div[@class, "item column-1"]//last::*//span//a'
    btn = driver.find_element(By.CSS_SELECTOR, f)
    print(btn.get_attribute('href'))


if __name__ == '__main__':
    main()
