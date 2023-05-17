from appium.webdriver import WebElement

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple) -> WebElement:
        return self.driver.find_element(*locator)

    def element_waiting(self, locator: tuple, timeout: int = 10) -> WebElement:
        return WebDriverWait(self.driver, timeout).until(expected_conditions.visibility_of_element_located(locator))

    def is_element_visible(self, locator: tuple) -> bool:
        element = self.element_waiting(locator)
        return element.is_displayed()

    def click_element(self, locator: tuple) -> None:
        element = self.element_waiting(locator)
        element.click()

    def fill_field(self, locator: tuple, text: str) -> None:
        element = self.element_waiting(locator)
        element.send_keys(text)
