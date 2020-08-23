from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class ConfirmationPage(BaseClass):
    country_search = (By.CSS_SELECTOR, "select[style='width: 200px;']")
    agree_button = (By.CSS_SELECTOR, "input[type='checkbox']")
    confirmation_button = (By.XPATH, "//button[text()='Proceed']")

    def __init__(self,driver):
        self.driver = driver

    def get_country_name(self):
        return self.driver.find_element(*ConfirmationPage.country_search)

    def click_agree_button(self):
        return self.driver.find_element(*ConfirmationPage.agree_button)

    def get_confirmation(self):
        return self.driver.find_element(*ConfirmationPage.confirmation_button)







