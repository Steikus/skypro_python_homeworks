from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/inputs")

sleep(2)
input = driver.find_element(By.CSS_SELECTOR, "input[type='number']")
input.send_keys("1000")
sleep(2)
input.clear()
input.send_keys("999")
sleep(2)

driver.quit()
