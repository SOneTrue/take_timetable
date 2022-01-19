from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()
    driver.get('https://btgp.ru/zameny-v-raspisanii.html')
    assert "Расписание занятий техникума и замены" in driver.title
    csspath_to_last_link = '//div[contains(@class, "item column-1")]/p[last()]//a'
    lastLink = driver.find_element(By.XPATH, csspath_to_last_link).get_attribute("href")
    print(lastLink)


if __name__ == '__main__':
    main()
