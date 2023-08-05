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


def test_hash_compatibility():
    pwd = Password(
        "x765H",
        "7b674cfd0b71cb81dfd9d34024ddf29d250c609ad33fb87adc644f284b214374",
    )
    expected = "f467b5a2a9a021e47a2a1d801ce8fdd42df058f6d5ed2abebd892174b7508645a113622abbc1ce3c636ecb4c5e844da29ceedf41d4d4f1456254be83478a6ead"  # noqa:E501
    assert pwd.hash == expected
