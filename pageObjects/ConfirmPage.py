from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class ConfirmPage(BaseClass):
    f_input = (By.CSS_SELECTOR, ".filter-input")
    c_list = (By.XPATH, "//div[@class='suggestions']/ul/li/a")
    c_box = (By.CSS_SELECTOR, "label[for='checkbox2']")
    submit = (By.CSS_SELECTOR, "input[type='submit']")
    msg = (By.CSS_SELECTOR, ".alert-success")
    c_name = "India"

    def __init__(self, driver):
        self.driver = driver

    def countryInput(self):
        return self.driver.find_element(*ConfirmPage.f_input)

    def countriesList(self):
        return self.driver.find_elements(*ConfirmPage.c_list)

    def checkBox(self):
        return self.driver.find_element(*ConfirmPage.c_box)

    def submitBtn(self):
        return self.driver.find_element(*ConfirmPage.submit)

    def msgText(self):
        return self.driver.find_element(*ConfirmPage.msg)