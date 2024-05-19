from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
wait = WebDriverWait(driver, 30)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

text = (By.CSS_SELECTOR, "p#text")

wait.until(
    EC.text_to_be_present_in_element(text, "Done!")
)

imgs = driver.find_elements(By.CSS_SELECTOR, "img")
i = len(imgs)
img = imgs[3]
attribute = img.get_attribute("src")
print(attribute)

driver.quit()
