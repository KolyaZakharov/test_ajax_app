import pytest

VALID_EMAIL = "qa.ajax.app.automation@gmail.com"
VALID_PASSWORD = "qa_automation_password"


@pytest.mark.parametrize(
    "email, password, result",
    [
        pytest.param(
            VALID_EMAIL,
            VALID_PASSWORD,
            True,
            id="correct pass and email"
        ),
        pytest.param(
            "invalid@gmail.com",
            VALID_PASSWORD,
            False,
            id="incorrect email only"
        ),
        pytest.param(
            VALID_EMAIL,
            "invalidpassword",
            False,
            id="incorrect pass only"
        ),
        pytest.param(
            "invalid@gmail.com",
            "invalidpassword",
            False,
            id="incorrect pass and email"
        ),
        pytest.param(
            VALID_EMAIL,
            "",
            False,
            id="empty pass field"
        ),
        pytest.param(
            "",
            VALID_PASSWORD,
            False,
            id="empty email field"
        ),
    ]
)
def test_user_login(user_login_fixture, email, password, result):
    page = user_login_fixture
    page.user_login(email, password)
    assert page.is_user_in_home_page() == result


