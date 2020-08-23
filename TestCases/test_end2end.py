import time
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from PageObjects.confirmationpage import ConfirmationPage
from PageObjects.homepage import HomePage
from PageObjects.pricepage import PricePage
from required_data.requireddatafortest import RequiredDataForTest
from utilities.BaseClass import BaseClass


class TestExample(BaseClass):
    #@pytest.mark.usefixtures("get_required_data")
    def test_end2end(self,get_required_data):
        self.driver.refresh()
        logger = self.calllogger()
        homepage = HomePage(self.driver)
        logger.info("going to send the data with required vegetable keyword..")
        homepage.get_data().send_keys("ca")
        logger.info("waiting for to get the suggestions to add into cart.")
        wait = WebDriverWait(self.driver,8)
        wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//h4[@class='product-name']")))
        products = homepage.get_product_names()
        i=-1
        for product in products:
            print(product.text)
            i=i+1
            if product.text == "Carrot - 1 Kg":
                add_cart = homepage.add_cart_products()
                add_cart[i].click()
                logger.info("selected the required vegetable or fruit."+product.text)
        homepage.click_add_cart_button().click()
        homepage.confirm_add_cart_option()[0].click()
        #here to check whether the given element to be there or not and if yes needs to send data.
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='Enter promo code']")))

        pricepage = PricePage(self.driver)
        logger.info("entering promocode")
        pricepage.get_promo_code().send_keys(get_required_data["promocode"])
        pricepage.click_promo_button().click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='promoInfo']")))
        promocode_confirm = pricepage.get_promo_confirmation()
        print("************************************")
        print(promocode_confirm.text)
        logger.info(promocode_confirm.text)
        print("************************************")
        assert "applied" in promocode_confirm.text
        pricepage.click_place_order().click()

        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[style='width: 200px;']")))
        confirmation_page = ConfirmationPage(self.driver)
        select = Select(confirmation_page.get_country_name())
        select.select_by_visible_text(get_required_data["country"])
        confirmation_page.click_agree_button().click()
        confirmation_page.get_confirmation().click()

    @pytest.fixture(params=RequiredDataForTest.test_page_data)
    def get_required_data(self, request):
        return request.param













