import pytest
from pages.bags_page import BagsPage

def test_title(driver):
    page = BagsPage(driver)
    assert page.title.is_displayed()