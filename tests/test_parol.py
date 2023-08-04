# pylint:disable=redefined-outer-name
import pytest

from parol import PASSWORD_LENGTH, Password


@pytest.fixture()
def password():
    return Password.generate()


def test_generate_password():
    password = Password.generate()

    assert len(password.password) == PASSWORD_LENGTH


def test_password_str():
    password = Password.generate()

    assert str(password) == "Password(password='***')"
    assert repr(password) == "Password(password='***')"


def test_invalid_password_length():
    with pytest.raises(ValueError, match="Invalid password length"):
        Password.generate(length=PASSWORD_LENGTH - 1)


def test_password_hash(password):
    new_password = Password(password=password.password, salt=password.salt)

    assert password.hash == new_password.hash


def test_validate(password):
    assert Password.validate(
        password=password.password,
        salt=password.salt,
        hash=password.hash,
    )


def test_eq():
    assert Password("123", "222") == Password("123", "222")
