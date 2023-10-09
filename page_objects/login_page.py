from datetime import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.ID, "username")
    __password_field = (By.NAME, "password")
    __submit_btn = (By.XPATH, "//button[@class='btn']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super().open_url(self.__url)

    def execute_login(self, username: str, password: str):
        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_btn)

        # ----the above method is used for the below code in an inheritance form
        # wait = WebDriverWait(self._driver, 10)
        # wait.until(ec.visibility_of_element_located(self.__username_field))
        # self._driver.find_element(self.__username_field).send_keys(username)
        #
        # # Type password into Password field
        # wait.until(ec.visibility_of_element_located(self.__password_field))
        # self._driver.find_element(self.__password_field).send_keys(password)
        #
        # # Push submit button
        # wait.until(ec.visibility_of_element_located(self.__submit_btn))
        # self._driver.find_element(self.__submit_btn).click()
