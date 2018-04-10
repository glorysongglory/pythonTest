from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument(
        'user-agent="Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19"')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')
    # page = driver.find_elements_by_xpath("//div[@class='pagerwg-button']")
    page = driver.find_elements_by_xpath("//div[@class='foldpagewg-text-con']")
    driver.execute_script('arguments[0].scrollIntoView();', page[-1])  # 拖动到可见的元素去
    page[-1].click()
    time.sleep(6)
    gomore = driver.find_elements_by_xpath("//div[@class='pagerwg-button']")
    while gomore[-1]:
        gomore[-1].click()
        gomore = driver.find_elements_by_xpath("//div[@class='pagerwg-button']")
        driver.execute_script('arguments[0].scrollIntoView();', gomore[-1])  # 拖动到可见的元素去
