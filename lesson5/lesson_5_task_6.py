from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def login_and_button(driver):
    driver.maximize_window()
    driver.get("http://the-internet.herokuapp.com/login")

    username = driver.find_element(By.CSS_SELECTOR, "input#username")
    password = driver.find_element(By.CSS_SELECTOR, "input#password")
    login = driver.find_element(By.CSS_SELECTOR, "button.radius")

    username.send_keys("tomsmith")
    password.send_keys("SuperSecretPassword!")
    login.click()

    sleep(5)


mozilla = webdriver.Firefox()
login_and_button(mozilla)
mozilla.quit()

google = webdriver.Chrome()
login_and_button(google)
google.quit()
