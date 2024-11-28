import time

from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self,driver):
        self.driver=driver


    shop=(By.XPATH,"//a[normalize-space()='Shop']")
    allProducts=(By.XPATH,"//h4[@class='card-title']")
    checkOutButton=(By.XPATH,"//a[@class='nav-link btn btn-primary']")

    def goToShopPage(self):
         self.driver.find_element(*HomePage.shop).click()
    def clickOnRequiredProduct(self,ProductName):
        allProduct=self.driver.find_elements(*HomePage.allProducts)
        productName = ProductName
        for product in allProduct:
            name = product.text
            if name == productName:
                self.driver.find_element(By.XPATH,
                                    "//a[.='" + productName + "']/../../..//button[@class='btn btn-info']").click()
        self.driver.find_element(*HomePage.checkOutButton).click()

