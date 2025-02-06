from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.about_us_link = page.locator(MainPageLocators.ABOUT_US_LINK)
        self.contacts_link = page.locator(MainPageLocators.CONTACTS_LINK)
        self.specialists_link = page.locator(MainPageLocators.SPECIALISTS_LINK)
        self.logo_link = page.locator(MainPageLocators.LOGO_LINK)

    def click_about_us(self):
        self.about_us_link.click()

    def click_contacts(self):
        self.contacts_link.click()

    def click_specialists(self):
        self.specialists_link.click()

    def click_logo(self):
        self.logo_link.click()
