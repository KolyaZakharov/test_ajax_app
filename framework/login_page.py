from appium.webdriver.common.appiumby import AppiumBy

from framework.page import Page


class LoginPage(Page):
    LOGIN_BUTTON_LOCATOR=(AppiumBy.ID, "com.ajaxsystems:id/login")
    EMAIL_FIELD_LOCATOR=(AppiumBy.ID, "com.ajaxsystems:id/login")
    PASSWORD_FIELD_LOCATOR=(AppiumBy.ID, "com.ajaxsystems:id/password")
    SUBMIT_BUTTON_LOCATOR=(AppiumBy.ID, "com.ajaxsystems:id/next")
    SIDE_BAR_LOCATOR = (AppiumBy.ID, "com.ajaxsystems:id/menuDrawer")

    def user_login(self, email: str, password: str) -> None:
        self.click_element(self.LOGIN_BUTTON_LOCATOR)
        self.fill_field(self.EMAIL_FIELD_LOCATOR, email)
        self.fill_field(self.PASSWORD_FIELD_LOCATOR, password)
        self.click_element(self.SUBMIT_BUTTON_LOCATOR)

    def is_user_in_home_page(self) -> bool:
        return self.is_element_visible(self.SIDE_BAR_LOCATOR)


