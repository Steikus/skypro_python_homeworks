from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/entry_ad")

close_button = driver.find_element(By.CSS_SELECTOR, "div.modal-footer")
sleep(1)
close_button.click()

print("Click")
sleep(1)
driver.quit()
