from selenium.webdriver.common.by import By


class CheckOut:
    def __init__(self,driver):
        self.driver=driver

    checkOutButton = (By.XPATH, "//button[normalize-space()='Checkout']")
    country=(By.XPATH , "//input[@id='country']")
    #driver.find_element(By.XPATH, "").send_keys("Ind")

    def orderPlacing(self,country):
        self.driver.find_element(*CheckOut.checkOutButton).click()
        self.driver.find_element(*CheckOut.country).send_keys(country)


