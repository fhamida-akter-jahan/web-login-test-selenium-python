# from datetime import time
import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestExceptions:

    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Verify Row 2 input field is displayed
        # row_2_input_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed but it's not"

    @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_element_not_interactable_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        #  Wait for the second row to load
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@id='row2']/input")))

        # Type text into the second input field
        row_2_input_element.send_keys("Sushi")

        # Push Save button using locator By.name(“Save”)
        # save_btn = driver.find_element(By.NAME, "Save")
        # save_btn.click()

        # you can write the comment out code above in a single line for one time call method
        driver.find_element(By.XPATH, "//div[@id='row2']/button[@name='Save']").click()

        # for my code both --find_element-- & --wait.until(ec.visibility_of_element_located)-- has passed the code
        # confirmation_element can also be written into below code for better structure
        # instead of presence_of_element_located --visibility_of_element_located-- is used as it will locate
        # only visible locators
        # Verify text saved
        # confirmation_element = driver.find_element(By.ID, "confirmation")

        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 2 was saved", "Confirmation is not expected"

    # the below code arises the --invalidelementstateexception--hence we rewrite the code
    # @pytest.mark.exceptions
    # @pytest.mark.debug
    # def test_invalid_element_state_exception(self, driver):
    #     # Open page
    #     driver.get("https://practicetestautomation.com/practice-test-exceptions/")
    #
    #     # Clear input field
    #     row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
    #     wait = WebDriverWait(driver, 10)
    #     wait.until(ec.element_to_be_clickable(row_1_input_element))
    #
    #     row_1_input_element.clear()
    #
    #     # Type text into the input field
    #     row_1_input_element.send_keys("Sushi")
    #
    #     # Verify text changed
    #     text = row_1_input_element.get_attribute("value")
    #     assert text == "Sushi", "Expected Sushi, but got" + text

    @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_invalid_element_state_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        time.sleep(5)

        # Clear input field
        row_1_edit_button = driver.find_element(By.ID, "edit_btn")
        row_1_edit_button.click()

        row_1_input_element = driver.find_element(By.XPATH, "//div[@id='row1']/input")
        wait = WebDriverWait(driver, 10)
        wait.until(ec.element_to_be_clickable(row_1_input_element))
        row_1_input_element.clear()

        # Type text into the input field
        row_1_input_element.send_keys("Sushi")

        row_1_save_button = driver.find_element(By.ID, "save_btn")
        row_1_save_button.click()

        # Verify text saved
        confirmation_element = wait.until(ec.visibility_of_element_located((By.ID, "confirmation")))
        confirmation_message = confirmation_element.text
        assert confirmation_message == "Row 1 was saved", "Confirmation message is not expected"

    @pytest.mark.exceptions
    # @pytest.mark.debug
    def test_stale_element_reference_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Find the instructions text element
        # instruction_element = driver.find_element(By.ID, "instructions")

        # Push add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # Verify instruction text element is no longer displayed
        wait = WebDriverWait(driver, 10)
        assert wait.until(ec.invisibility_of_element_located(
            (By.ID, "instructions"))), "Instruction should text element not be displayed"
        # assert not instruction_element.is_displayed(), "Instruction should text element not be displayed"

    @pytest.mark.exceptions
    @pytest.mark.debug
    def test_timeout_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        # Wait for 3 seconds for the second input field to be displayed
        wait = WebDriverWait(driver, 6)
        row_2_input_element = wait.until(ec.visibility_of_element_located(
            (By.XPATH, "//div[@id='row2']/input"))), "Failed waiting for Row 2 input visible "

        # Verify second input field is displayed
        # row_2_input_locator = driver.find_element(By.XPATH, "//div[@id='row2']/input")
        assert row_2_input_element.is_displayed(), "Row 2 input should be displayed but it's not"
