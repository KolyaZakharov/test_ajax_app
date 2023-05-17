from framework import LoginPage


class Sidebar(LoginPage):

    def open_draw_menu(self) -> None:
        self.click_element(self.SIDE_BAR_LOCATOR)
