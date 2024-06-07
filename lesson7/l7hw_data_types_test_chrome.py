from selenium import webdriver
import pytest
from pages.main_data import MainData
from pages.result_page import ResultPage


@pytest.fixture(scope='module')
def driver():
    browser = webdriver.Chrome()
    main_page = MainData(browser)
    main_page.add_data()
    main_page.submit_button()
    yield browser
    browser.quit()


@pytest.mark.parametrize('element, expect_color', [("div#first-name", "rgba(15, 81, 50, 1)"), ("div#last-name", "rgba(15, 81, 50, 1)"),
("div#address", "rgba(15, 81, 50, 1)"), ("div#city", "rgba(15, 81, 50, 1)"), ("div#country", "rgba(15, 81, 50, 1)"), ("div#e-mail", "rgba(15, 81, 50, 1)"),
("div#phone", "rgba(15, 81, 50, 1)"), ("div#job-position", "rgba(15, 81, 50, 1)"), ("div#company", "rgba(15, 81, 50, 1)")])
def test_green_alerts(driver, element, expect_color):
    result_page = ResultPage(driver)
    color = result_page.check_element_color(element)
    assert color == expect_color


@pytest.mark.parametrize('element', ["div#zip-code"])
def test_red_alert(driver, element):
    result_page = ResultPage(driver)
    color = result_page.check_element_color(element)
    assert color != "rgba(15, 81, 50, 1)", "This one is red"
