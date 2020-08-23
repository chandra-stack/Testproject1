from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class PricePage(BaseClass):
    promo_code = (By.CSS_SELECTOR, "input[placeholder='Enter promo code']")
    promo_button = (By.CSS_SELECTOR, "button[class='promoBtn']")
    promo_code_confirmation = (By.XPATH, "//span[@class='promoInfo']")
    place_order_button = (By.XPATH, "//button[text()='Place Order']")

    def __init__(self, driver):
        self.driver = driver

    def get_promo_code(self):
        return self.driver.find_element(*PricePage.promo_code)

    def click_promo_button(self):
        return self.driver.find_element(*PricePage.promo_button)

    def get_promo_confirmation(self):
        return self.driver.find_element(*PricePage.promo_code_confirmation)

    def click_place_order(self):
        return self.driver.find_element(*PricePage.place_order_button)




