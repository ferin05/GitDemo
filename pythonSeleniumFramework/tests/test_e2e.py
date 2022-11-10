from time import sleep

import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import LoginPage
from pageObjects.TradePage import TradePage
from testLoginData.TestLoginData import TestData
from utilities.BaseClass import BaseClass


class TestE2E(BaseClass):
    def test_end_to_end(self, data_load):
        login = LoginPage(self.driver)
        login.get_username().send_keys(data_load["username"])
        login.get_password().send_keys(data_load["password"])
        login.get_rememberUserId().click()
        login.get_accept().click()
        trade = TradePage(self.driver)
        trade.get_trade_button().click()
        trade.get_symbol().send_keys("TW")
        trade.get_symbol_lookup().click()
        trade.get_side().click()
        trade.get_quantity().click()
        for i in range(3):
            trade.get_quantity_input().send_keys(Keys.BACK_SPACE)
        trade.get_quantity_input().send_keys(15)
        sleep(1)
        trade.get_review().click()
        trade.get_send().click()
        trade.get_notification().click()
        trade.get_order_confirmation()
        sleep(2)
        login.get_logout_button().click()
        print("chnages")
        print("chnages1")
        print("chnages2")

    @pytest.fixture(params=TestData.test_data)
    def data_load(self, request):
        return request.param




        # self.driver.find_element(By.XPATH, "//input[@type='number']").click()
        # for i in range(3):
        #     self.driver.find_element(By.XPATH, "//input[@type='number']").send_keys(Keys.BACK_SPACE)
        # self.driver.find_element(By.XPATH, "//input[@type='number']").send_keys(15)
        # self.driver.find_element(By.XPATH, "//button[@data-testid='trade-page-button']").click()
        # self.driver.find_element(By.ID, "navigation-symbol-search").send_keys("TW")
        # self.driver.find_element(By.XPATH, "//span[text()='TRADEWEB MARKETS INC COM CL A']").click()
        # self.driver.find_element(By.XPATH, ""//span[text()='TRADEWEB MARKETS INC COM CL A']").click()
        # self.driver.find_element(By.CSS_SELECTOR, "#review-order-button").click
        # self.driver.find_element(By.CSS_SELECTOR, "#send-order-button").click
        # self.driver.find_element(By.XPATH, "//div[text()= 'Notifications']").click
        # original_confirmation = []
        # original_message = [
        #     self.driver.find_element(By.XPATH, "(//div[@class='NotificationCardStyled__Text-liTWMR fhanmg'])[1]").text()
        #  print(original_message)
        #     for records in original_message:
        #         original_confirmation.append(records)
        #     print(original confirmation)
        #     assert original_message == original_confirmation
        # self.driver.find_element(By.ID, "username0").send_keys("ferinstinson1")
        # self.driver.find_element(By.ID, "password1").send_keys("Archie2021!")
        # self.driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
        # self.driver.find_element(By.CLASS_NAME, "accept").click()
        # self.driver.find_element(By.ID, "review-order-button").click()
        # self.driver.find_element(By.ID, "send-order-button").click()
        # self.driver.find_element(By.XPATH, "(//div[@class='NotificationCardstyle']").click()
        # # original_confirmation = []
        # # original_message = self.driver.find_element(By.XPATH)
