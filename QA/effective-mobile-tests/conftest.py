import pytest
from playwright.sync_api import Page, sync_playwright

@pytest.fixture(scope="function")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Запуск браузера
        page = browser.new_page()
        yield page
        browser.close()