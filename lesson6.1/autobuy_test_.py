from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

def test_check_summary(browser):
    WebDriverWait(browser, 30)
    browser.get("https://www.saucedemo.com/")
    browser.find_element(By.CSS_SELECTOR, "input#user-name").send_keys("standard_user")
    browser.find_element(By.CSS_SELECTOR, "input#password").send_keys("secret_sauce")
    browser.find_element(By.CSS_SELECTOR, "input#login-button").click()
    browser.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-backpack").click()
    browser.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-bolt-t-shirt").click()
    browser.find_element(By.CSS_SELECTOR, "button#add-to-cart-sauce-labs-onesie").click()
    browser.find_element(By.CSS_SELECTOR, "a.shopping_cart_link").click()
    browser.find_element(By.CSS_SELECTOR, "button#checkout").click()
    browser.find_element(By.CSS_SELECTOR, "input#first-name").send_keys("Vlad")
    browser.find_element(By.CSS_SELECTOR, "input#last-name").send_keys("IsLove")
    browser.find_element(By.CSS_SELECTOR, "input#postal-code").send_keys("123456")
    browser.find_element(By.CSS_SELECTOR, "input#continue").click()
    total = browser.find_element(By.CSS_SELECTOR, "div.summary_total_label").text
    assert "58.29" in total
