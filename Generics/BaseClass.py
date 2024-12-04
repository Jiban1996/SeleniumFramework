import pytest

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup_driver")
class BaseClass:

    def waitUntilElement(self,ele):
        w = WebDriverWait(self.driver, 10)
        w.until(expected_conditions.presence_of_element_located(ele))