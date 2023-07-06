from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login(d):
    d.find_element(By.ID, "user-name").send_keys("standard_user")
    d.find_element(By.ID, "password").send_keys("secret_sauce")
    d.find_element(By.ID, "login-button").click()
