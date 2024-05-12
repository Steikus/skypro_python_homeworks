from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
url = "http://uitestingplayground.com/classattr"

for b in range(3):
    driver.get(url)
    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    sleep(2)
    button.click()
    alert = driver.switch_to.alert
    print(alert.text)
    sleep(2)
    alert.accept()

driver.quit()
