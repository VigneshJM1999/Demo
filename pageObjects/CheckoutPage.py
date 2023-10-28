from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


class CheckoutPage(BaseClass):
    titles = (By.CSS_SELECTOR, ".card-title")
    footers = (By.CSS_SELECTOR, ".card-footer")
    btn_primary = (By.CSS_SELECTOR, ".btn-primary")
    btn_success = (By.CSS_SELECTOR, ".btn-success")

    def __init__(self, driver):
        self.driver = driver

    def cardItems(self):
        return self.driver.find_elements(*CheckoutPage.titles)

    def cart(self):
        return self.driver.find_elements(*CheckoutPage.footers)

    def chekoutBtn(self):
        return self.driver.find_element(*CheckoutPage.btn_primary)

    def successBtn(self):
        self.driver.find_element(*CheckoutPage.btn_success).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage


