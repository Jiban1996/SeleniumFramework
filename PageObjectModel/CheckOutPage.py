import time

from selenium.webdriver.common.by import By

from Generics import BaseClass


class CheckOut:
    def __init__(self,driver):
        self.driver=driver

    checkOutButton = (By.XPATH, "//button[normalize-space()='Checkout']")
    country=(By.XPATH , "//input[@id='country']")
    countryLink=(By.XPATH,"//a[.='India']")

    def orderPlacing(self,country):
        self.driver.find_element(*CheckOut.checkOutButton).click()
        self.driver.find_element(*CheckOut.country).send_keys(country)
        #time.sleep(10)
        BaseClass.BaseClass.waitUntilElement(*CheckOut.countryLink)
        self.driver.find_element(*CheckOut.countryLink).click()




