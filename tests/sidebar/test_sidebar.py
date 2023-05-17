import pytest
from appium.webdriver.common.appiumby import AppiumBy

ADD_HUB_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/addHub")
SETTINGS_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/settings")
HELP_BUTTON = (AppiumBy.ID, "com.ajaxsystems:id/help")
REPORT_PROBLEM = (AppiumBy.ID, "com.ajaxsystems:id/logs")
TERMS_SERVICE = (AppiumBy.ID, "com.ajaxsystems:id/documentation_text")
SIDE_BAR_LOCATOR = (AppiumBy.ID, "com.ajaxsystems:id/menuDrawer")


@pytest.mark.parametrize(
    "button", [
        pytest.param(
            SETTINGS_BUTTON,
            id="Settings button in sidebar",
        ),
        pytest.param(
            ADD_HUB_BUTTON,
            id="add hub button in sidebar",
        ),
        pytest.param(
            HELP_BUTTON,
            id="help button in sidebar",
        ),
        pytest.param(
            TERMS_SERVICE,
            id="terms service button in sidebar",
        ),
        pytest.param(
            REPORT_PROBLEM,
            id="report button in sidebar",
        ), ],
)
def test_button_in_sidebar(sidebar_fixture, button):
    page = sidebar_fixture
    sidebar_fixture.click_element(SIDE_BAR_LOCATOR)
    assert page.find_element(button)
