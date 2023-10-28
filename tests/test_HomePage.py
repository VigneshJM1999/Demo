import pytest

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestExample(BaseClass):

    def test_formSubmission(self, getData):
        log = self.Logger()
        homepage = HomePage(self.driver)
        homepage.formName().send_keys(getData["Name"])
        log.info("Name is : "+getData["Name"])
        homepage.formEmail().send_keys(getData["Email"])
        log.info("Email is : "+getData["Email"])
        homepage.formPassword().send_keys(getData["Password"])
        log.info("Password is : "+str(getData["Password"]))
        homepage.formCheckbox1().click()
        self.selectText(homepage.formDropdown(), getData["Gender"])
        log.info("Gender is : "+getData["Gender"])
        homepage.formSubmit().click()
        message = homepage.formAlert().text
        log.info(message)
        assert "Success" in message
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.getExcelData("TestCase2"))
    def getData(self, request):
        return request.param
