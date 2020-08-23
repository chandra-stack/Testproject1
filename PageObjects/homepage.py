from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class HomePage(BaseClass):
    search_data= (By.CSS_SELECTOR, "input[type='search']")
    product_names = (By.XPATH, "//h4[@class='product-name']")
    add_cart = (By.XPATH, "//div[@class='product-action']")
    add_cart_button = (By.CSS_SELECTOR, "img[alt='Cart']")
    confirm_add_cart_button = (By.XPATH, "//div[@class='action-block']/button")

    def __init__(self, driver):
        self.driver = driver

    def get_data(self):
        return self.driver.find_element(*HomePage.search_data)

    def get_product_names(self):
        return self.driver.find_elements(*HomePage.product_names)

    def add_cart_products(self):
        return self.driver.find_elements(*HomePage.add_cart)

    def click_add_cart_button(self):
        return self.driver.find_element(*HomePage.add_cart_button)

    def confirm_add_cart_option(self):
        return self.driver.find_elements(*HomePage.confirm_add_cart_button)









