from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Firefox()
wait = WebDriverWait(driver, 15)
driver.get("http://uitestingplayground.com/textinput")

button_name = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
button_name.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "#updatingButton")
button.click()
wait.until(
    lambda driver: button.text == "SkyPro"
)
print(button.text)

driver.quit()
