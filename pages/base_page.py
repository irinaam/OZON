from urllib.parse import urlparse

class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path
