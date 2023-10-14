import time

import pytest
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage


class TestNegativeScenarios:

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("incorrectUser", "Password123", "Your username is invalid!"),
                              ("student", "incorrectPassword", "Your password is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.execute_login(username, password)
        assert login_page.get_error_message() == expected_error_message, "Error message is not expected"

    def test_negative_username(self, driver):
        # Go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")
        # Type username incorrectUser into Username field
        username_locator = driver.find_element(By.ID, "username")
        username_locator.send_keys("incorrectUser")
        # username_locator.send_keys("student")

        # Type password Password123 into Password field
        password_locator = driver.find_element(By.NAME, "password")
        password_locator.send_keys("Password123")

        # Punch Submit button
        submit_btn_locator = driver.find_element(By.XPATH, "//button[@class='btn']")
        submit_btn_locator.click()
        time.sleep(2)

        # Verify error message is displayed
        error_message_locator = driver.find_element(By.ID, "error")
        assert error_message_locator._is_displayed(), "error message is not displayed but it should "

        # Verify error message  text is Your username is invalid!
        error_message = error_message_locator.text
        assert error_message == "Your username is invalid!", "Error message is not expected"
