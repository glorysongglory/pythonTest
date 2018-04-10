from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    driver = webdriver.Chrome("D:\\soft\\chromedriver.exe")
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    print(driver.page_source)
