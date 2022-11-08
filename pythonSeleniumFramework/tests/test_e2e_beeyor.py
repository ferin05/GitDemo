
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from pageObjects.ShoppingBeeyor import ShoppingBeeyor
from utilities.BaseClass import BaseClass


class TestBeeyor(BaseClass):
    def test_e2e_beeyor(self):
        shopping = ShoppingBeeyor(self.driver)
        shopping.get_list_of_items()
        shopping.get_item()





# list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")
# if expected_conditions.presence_of_element_located(driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Add “Belt” to your cart"]')):
#     exclude_items = driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Add “Belt” to your cart"]')
#     for i in list_of_items:
#      if i == exclude_items:
#       list_of_items.remove(exclude_items)
# for item in list_of_items:
#     item.click()
#     if item == driver.find_element(By.XPATH, "(//a[text()='Add to cart'])[7]"):
#         break
# sleep(2)
# actions = ActionChains(driver)
# actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[class= 'cart-contents']")).perform()
# sleep(2)
# actions.move_to_element(driver.find_element(By.CSS_SELECTOR, "a[class= 'button wc-forward']")).click().perform()
# driver.find_element(By.CSS_SELECTOR, 'input[name="coupon_code"]').send_keys("tojtech automation")
# sleep(1)
# driver.find_element(By.XPATH, '//button[@name="apply_coupon"]').click()
# wait = WebDriverWait(driver, 10)
# test = (driver.find_element(By.XPATH,"//td[@data-title='Total']//bdi[1]").text)
# sleep(3)
# print(test)
# wait.until(expected_conditions.presence_of_element_located(By.XPATH, "//td[@data-title='Total']//bdi[1]"))
# amount = 124.00
# discount = amount * 0.10
# total = amount - discount
# discount = 124.00 * 0.10
# total = [124 - discount]
# # print(total)
# for records in test:
#     total.append(records)
# assert test == total
