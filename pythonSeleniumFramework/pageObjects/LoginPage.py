# self.driver.find_element(By.ID, "username0").send_keys("ferinstinson1")
# self.driver.find_element(By.ID, "password1").send_keys("Archie2021!")
# self.driver.find_element(By.XPATH, "//label[@for='rememberuserid']").click()
# self.driver.find_element(By.CLASS_NAME, "accept").click()
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.XPATH, "//input[@type='text']")
    password = (By.ID, "password1")
    rememberUserId = (By.XPATH, "//label[@for='rememberuserid']")
    accept = (By.CLASS_NAME, "accept")
    logout_button = (By.XPATH,"//div[text()='Log Out']")

    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_rememberUserId(self):
        return self.driver.find_element(*LoginPage.rememberUserId)

    def get_accept(self):
        return self.driver.find_element(*LoginPage.accept)

    def get_logout_button(self):
        return self.driver.find_element(*LoginPage.logout_button)


