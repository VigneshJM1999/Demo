from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckoutPage
from utilities.BaseClass import BaseClass


class HomePage(BaseClass):
    shop = (By.CSS_SELECTOR, "a[href*='shop']")
    name = (By.CSS_SELECTOR, "input[name='name']")
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    checkbox1 = (By.ID, "exampleCheck1")
    dropdown = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert =(By.CLASS_NAME, "alert-success")

    def __init__(self, driver):
        self.driver = driver

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage

    def formName(self):
        return self.driver.find_element(*HomePage.name)

    def formEmail(self):
        return self.driver.find_element(*HomePage.email)

    def formPassword(self):
        return self.driver.find_element(*HomePage.password)

    def formCheckbox1(self):
        return self.driver.find_element(*HomePage.checkbox1)

    def formDropdown(self):
        return self.driver.find_element(*HomePage.dropdown)

    def formSubmit(self):
        return self.driver.find_element(*HomePage.submit)

    def formAlert(self):
        return self.driver.find_element(*HomePage.alert)