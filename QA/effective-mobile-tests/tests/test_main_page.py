from pytest import fixture
from playwright.sync_api import Page
from pages.main_page import MainPage


@fixture
def main_page(page: Page):
    return MainPage(page)


def test_navigate_to_about_us(main_page):
    main_page.navigate("https://effective-mobile.ru")
    main_page.click_about_us()
    assert main_page.get_current_url() == "https://effective-mobile.ru/#about"


def test_navigate_to_contacts(main_page):
    main_page.navigate("https://effective-mobile.ru")
    main_page.click_contacts()
    assert main_page.get_current_url() == "https://effective-mobile.ru/#contacts"


def test_navigate_to_specialists(main_page):
    main_page.navigate("https://effective-mobile.ru")
    main_page.click_specialists()
    assert main_page.get_current_url() == "https://effective-mobile.ru/#specialists"


def test_navigate_to_main_page_via_logo(main_page):
    main_page.navigate("https://effective-mobile.ru/#about")
    main_page.click_logo()
    assert main_page.get_current_url() == "https://effective-mobile.ru/"
