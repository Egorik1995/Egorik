from pytest import fixture
from playwright.sync_api import Page
from pages.main_page import MainPage


@fixture
def main_page(page: Page):
    return MainPage(page)


def test_navigate_to_about_us(main_page):
    main_page.navigate("https://effective-mobile.ru")

    if section == "about":
        main_page.click_about_us()
    elif section == "contacts":
        main_page.click_contacts()
    elif section == "specialists":
        main_page.click_specialists()

    assert main_page.get_current_url() == expected_url

def test_navigate_to_main_page_via_logo(main_page):
    main_page.navigate("https://effective-mobile.ru/#about")
    main_page.click_logo()
    assert main_page.get_current_url() == "https://effective-mobile.ru/"
