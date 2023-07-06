from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pages import base_page


## To run "python -m pytest"

driver = webdriver.Chrome()

b = base_page.BasePage(driver)
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
driver.implicitly_wait(3)


# LOGIN
def test_login():
    b.set(locator=(By.ID, "user-name"), value="standard_user")
    b.set(locator=(By.ID, "password"), value="secret_sauce")
    b.click(locator=(By.ID, "login-button"))
    time.sleep(3)


def test_buy_items():
    # Add Items To Cart
    b.select_element(
        locator=(By.XPATH, "//select[@class='product_sort_container']"),
        type="select_by_value",
        type_val="az",
    )
    all_items = b.find_2(By.CLASS_NAME, "inventory_item")
    if len(all_items) > 0:
        bag_pack = all_items[0]
        jacket = all_items[3]
        bag_pack.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        jacket.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
    else:
        print("Not Enough Items!")

    # Open Cart
    b.click(locator=(By.CLASS_NAME, "shopping_cart_link"))
    b.scroll_down(driver)

    time.sleep(2)

    # Checkout
    b.click(locator=(By.ID, "checkout"))
    b.scroll_down(driver)

    time.sleep(2)

    # Add Customer details
    b.set(locator=(By.ID, "first-name"), value="Mark")
    b.set(locator=(By.ID, "last-name"), value="Smith")
    b.set(locator=(By.ID, "postal-code"), value="123456")
    b.scroll_down(driver)
    b.click(locator=(By.ID, "continue"))

    time.sleep(2)

    # Finish
    b.click(locator=(By.ID, "finish"))
    b.scroll_down(driver)

    time.sleep(3)


# Logout
def test_logout():
    b.click(locator=(By.ID, "react-burger-menu-btn"))
    b.click(locator=(By.ID, "logout_sidebar_link"))

    time.sleep(3)
