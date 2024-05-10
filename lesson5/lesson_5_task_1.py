from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")


for button in range(5):
    button = driver.find_element(By.CSS_SELECTOR,
                                 "button[onclick='addElement()']")
    button.click()

sleep(3)

delete = driver.find_elements(By.CSS_SELECTOR,
                              "button.added-manually")
print(len(delete))

driver.quit()
