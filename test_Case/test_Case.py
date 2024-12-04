import time

from selenium.webdriver.common.by import By

from Generics.BaseClass import  BaseClass
from PageObjectModel.CheckOutPage import CheckOut
from PageObjectModel.HomePage import HomePage


class Test_Example(BaseClass):
    def test_sample(self):
        driver=self.driver

        Home=HomePage(driver)
        Home.goToShopPage()
        productName = "Samsung Note 8"
        Home.clickOnRequiredProduct(productName)
        time.sleep(3)

        CountryName="India"
        Check=CheckOut(driver)
        Check.orderPlacing(CountryName)


        #driver.find_element(By.XPATH, "//a[.='India']").click()
        driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        print(msg)

        assert "Success! Thank you!" in msg

        time.sleep(5)

