from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture(scope='module')
def browser():
    driver = webdriver.Firefox()
    WebDriverWait(driver, 30)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys("")
    driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    yield driver
    driver.quit()


@pytest.mark.parametrize('element, expect_color', [("div#first-name", "rgb(15, 81, 50)"), ("div#last-name", "rgb(15, 81, 50)"),
("div#address", "rgb(15, 81, 50)"), ("div#city", "rgb(15, 81, 50)"), ("div#country", "rgb(15, 81, 50)"), ("div#e-mail", "rgb(15, 81, 50)"),
("div#phone", "rgb(15, 81, 50)"), ("div#job-position", "rgb(15, 81, 50)"), ("div#company", "rgb(15, 81, 50)")])
def test_green_fields(browser, element, expect_color):
    driver = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, element)))
    color = driver.value_of_css_property("color")
    assert color == expect_color


def test_red_field(browser):
    driver = WebDriverWait(browser, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "div#zip-code")))
    color = driver.value_of_css_property("color")
    assert color != "rgb(15, 81, 50)", "This one is red"
