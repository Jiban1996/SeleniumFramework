# conftest.py
import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup_driver(request):
    # Initialize the WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://rahulshettyacademy.com/angularpractice/")

    # Attach the driver to the test class
    request.cls.driver = driver
    yield
    driver.quit()  # Ensure the driver is closed after tests