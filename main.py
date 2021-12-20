import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestAddUser:
    @pytest.fixture(autouse=True)
    def set_up(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self):
        self.driver.quit()

    def test_add_new_user(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        self.driver.find_element(By.ID, "txtUsername").send_keys("Admin")
        self.driver.find_element(By.ID, "txtPassword").send_keys("admin123")
        self.driver.find_element(By.ID, "btnLogin").click()
        self.driver.find_element(By.ID, "menu_admin_viewAdminModule").click()
        self.driver.find_element(By.ID, "btnAdd").click()
        self.driver.find_element(By.ID, "systemUser_userName").send_keys("abcabcabc")
        self.driver.find_element(By.ID, "systemUser_password").send_keys("stasystasy")
        self.driver.find_element(By.ID, "systemUser_confirmPassword").send_keys("stasystasy")
        self.driver.find_element(By.ID, "systemUser_employeeName_empName").send_keys("Cecil Bonaparte")
        time.sleep(1)
        self.driver.find_element(By.ID, "btnSave").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "searchSystemUser_userName").send_keys("abcabcabc")
        self.driver.find_element(By.ID, "searchBtn").click()

        time.sleep(1)
        self.driver.find_element(By.XPATH, "//tr[td[a[contains(text(),\'abcabcabc\')]]]")
        time.sleep(1)
        self.driver.find_element(By.ID, "resetBtn").click()
        time.sleep(1)

        self.driver.find_element(By.XPATH, "//tr[td[a[contains(text(),\'abcabcabc\')]]]//input").click()
        self.driver.find_element(By.ID, "btnDelete").click()
        self.driver.find_element(By.ID, "dialogDeleteBtn").click()

if __name__ == "__main__":
    pytest.main()
