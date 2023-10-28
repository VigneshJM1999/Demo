from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.Logger()
        homepage = HomePage(self.driver)
        checkoutpage = homepage.shopItems()
        log.info("Getting all product Names")
        tmpList = checkoutpage.cardItems()
        i = -1
        for j in tmpList:
            i += 1
            name = j.text
            log.info(name)
            if name == "Nokia Edge":
                checkoutpage.cart()[i].click()
                break
        checkoutpage.chekoutBtn().click()
        confirmpage = checkoutpage.successBtn()
        confirmpage.countryInput().send_keys(confirmpage.c_name)
        log.info("Entering country name")
        self.verifyLinkPresence("suggestions")
        countryList = confirmpage.countriesList()
        for i in countryList:
            if i.text == "India":
                i.click()
                break
        confirmpage.checkBox().click()
        confirmpage.submitBtn().click()
        msg = confirmpage.msgText().text
        log.info(msg)
        assert "Success" in msg
