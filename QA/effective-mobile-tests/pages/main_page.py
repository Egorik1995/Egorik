from .base_page import BasePage

class MainPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.about_us_link = page.locator("a[href='#about']")
        self.contacts_link = page.locator("a[href='#contacts']")
        self.specialists_link = page.locator("a[href='#specialists']")
        self.logo_link = page.locator("a.logo")

    def click_about_us(self):
        self.about_us_link.click()

    def click_contacts(self):
        self.contacts_link.click()

    def click_specialists(self):
        self.specialists_link.click()

    def click_logo(self):
        self.logo_link.click()