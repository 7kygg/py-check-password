import pytest

from app.main import check_password


@pytest.mark.parametrize(
    "password,expected",
    [
        pytest.param(
            "Pass@word1",
            True,
            id="test_password_is_valid"
        ),
        pytest.param(
            "Pss@1",
            False,
            id="test_password_length_is_less_than_8_symbols"
        ),
        pytest.param(
            "Pass@word1Pass@word",
            False,
            id="test_password_length_is_more_than_16_symbols"
        ),
        pytest.param(
            "Password1",
            False,
            id="test_password_should_contain_at_least_1_special_character"
        ),
        pytest.param(
            "Password@",
            False,
            id="test_should_contain_at_least_1_digit"
        ),
        pytest.param(
            "password1@",
            False,
            id="test_should_contain_at_least_1_uppercase_letter"
        ),
        pytest.param(
            "Pass@word1:*Я",
            False,
            id="test_password_cannot_contain_not_allowed_symbols"
        ),
        pytest.param(
            "PassW01@",
            True,
            id="test_if_password_length_is_8_symbols"
        ),
        pytest.param(
            "PasswordPasswo1@",
            True,
            id="test_if_password_length_is_16_symbols"
        )
    ]
)
def test_check_different_passwords(password: str, expected: bool) -> None:
    assert check_password(password) == expected
