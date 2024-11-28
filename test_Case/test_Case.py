import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Generics.BaseClass import baseClass
from PageObjectModel.CheckOutPage import CheckOut
from PageObjectModel.HomePage import HomePage


class Test_Example(baseClass):
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

        w = WebDriverWait(driver, 10)
        w.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[.='India']")))
        driver.find_element(By.XPATH, "//a[.='India']").click()
        driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        msg = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        print(msg)

        assert "Success! Thank you!" in msg

        time.sleep(5)

