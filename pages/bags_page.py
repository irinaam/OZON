from .base_page import BasePage
from selenium.webdriver.common.by import By

class BagsPage(BasePage):
    def __init__(self, driver):
        super().__init__(self, driver)
        url = 'https://www.ozon.ru/category/sumki-zhenskie-17001/'
        driver.get(url)
        self.title = driver.find_element(By.TAG_NAME,'h1')