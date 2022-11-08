from selenium.webdriver.common.by import By
# list_of_items = driver.find_elements(By.XPATH, "//a[text()='Add to cart']")


class ShoppingBeeyor:
    def __init__(self, driver):
        self.driver = driver

    list_of_items = (By.XPATH, "//a[text()='Add to cart']")
    item = (By.XPATH, "(//a[text()='Add to cart'])[7]")

    def get_list_of_items(self):
        return self.driver.find_element(*ShoppingBeeyor.list_of_items)

    def get_item(self):
        return self.driver.find_element(*ShoppingBeeyor.item)
