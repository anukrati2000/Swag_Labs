from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BasePage:
    """
    The Purpose Of A BasePage Is To Contain Methods Common To All Page Objects
    """

    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def find_2(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.find(*locator).click()
        # self.driver.find_element(*locator).click()

    def set(self, locator, value):
        self.find(*locator).clear()
        self.find(*locator).send_keys(value)

    def get_text(self, locator):
        return self.find(*locator).text

    def get_title(self):
        return self.driver.title

    def select_element(self, locator, type, type_val):
        dropdown = Select(self.find(*locator))
        if type == "select_by_value":
            dropdown.select_by_value(type_val)
        elif type == "select_by_index":
            dropdown.select_by_index(type_val)
        else:
            dropdown.select_by_visible_text(type_val)

    def scroll_down(self, driver):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
