from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.implicitly_wait(4)
driver.get("http://uitestingplayground.com/textinput")

button_name = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
button_name.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()
print(button.text)

driver.quit()
