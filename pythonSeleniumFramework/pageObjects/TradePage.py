from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TradePage:
    def __init__(self, driver):
        self.driver = driver

    trade_button = (By.XPATH, "//button[@data-testid='trade-page-button']")
    symbol = (By.ID, "navigation-symbol-search")
    symbol_lookup = (By.XPATH, "//span[text()='TRADEWEB MARKETS INC COM CL A']")
    side = (By.CSS_SELECTOR, "button[data-testid='TradeButton-buy']")
    quantity = (By.XPATH, "//input[@type='number']")
    review = (By.CSS_SELECTOR, "#review-order-button")
    send = (By.CSS_SELECTOR, "#send-order-button")
    notification = (By.XPATH, "//div[text()= 'Notifications']")
    original_notification = (By.XPATH, "(//div[@class='NotificationCardstyled__Text-liTWMR fhanmg'])[1]")

    def get_trade_button(self):
        return self.driver.find_element(*TradePage.trade_button)

    def get_symbol(self):
        return self.driver.find_element(*TradePage.symbol)

    def get_symbol_lookup(self):
        return self.driver.find_element(*TradePage.symbol_lookup)

    def get_side(self):
        return self.driver.find_element(*TradePage.side)

    def get_quantity(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_quantity_input(self):
        return self.driver.find_element(*TradePage.quantity)

    def get_review(self):
        return self.driver.find_element(*TradePage.review)

    def get_send(self):
        return self.driver.find_element(*TradePage.send)

    def get_notification(self):
        return self.driver.find_element(*TradePage.notification)

    def get_order_confirmation(self):
        original_confirmation = []
        original_message = [
            self.driver.find_element(*TradePage.original_notification).text]
        for records in original_message:
            original_confirmation.append(records)
            assert original_message == original_confirmation
        return original_message

    # self.driver.find_element(By.XPATH, "//button[@data-testid='trade-page-button']").click()
    # self.driver.find_element(By.ID, "navigation-symbol-search").send_keys("TW")
    # for i in range(3):
    #     self.driver.find_element(By.XPATH, "//input[@type='number']").send_keys(Keys.BACK_SPACE)
    # self.driver.find_element(By.XPATH, "//input[@type='number']").send_keys(15)
    # self.driver.find_element(By.CSS_SELECTOR, "#review-order-button").click
    # self.driver.find_element(By.CSS_SELECTOR, "#send-order-button").click
    # self.driver.find_element(By.XPATH, "//div[text()= 'Notifications']").click
