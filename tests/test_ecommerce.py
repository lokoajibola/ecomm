import pytest
from selenium import webdriver
# from ..pages.login_page import LoginPage
from pages.login_page import LoginPage  # Assuming your package is named 'ecommerce'
# from pages.inventory_page import InventoryPage
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()


def test_ecommerce_flow(driver):
    # Login
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"
