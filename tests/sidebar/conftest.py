import pytest

from framework.sidebar import Sidebar

VALID_EMAIL = "qa.ajax.app.automation@gmail.com"
VALID_PASSWORD = "qa_automation_password"


@pytest.fixture(scope='module')
def sidebar_fixture(driver):
    sidebar = Sidebar(driver)
    sidebar.user_login(VALID_EMAIL, VALID_PASSWORD)
    yield sidebar


