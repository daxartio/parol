from parol.bcrypt import Password


def test_password_hash():
    assert Password(b"123").hash()


def test_password_eq():
    assert Password(b"123") == Password(b"123")


def test_password_str():
    password = Password(b"123")

    assert str(password) == "Password(password='***')"
    assert repr(password) == "Password(password='***')"


def test_password_hash_diff():
    pwd = Password(b"123")
    assert pwd.hash() != pwd.hash()


def test_password_validate():
    pwd = Password(b"123")
    pwd_hash1 = pwd.hash()
    pwd_hash2 = pwd.hash()
    assert Password.validate(pwd.password, pwd_hash1)
    assert Password.validate(pwd.password, pwd_hash2)


def test_hash_compatibility():
    pwd = b"123"
    pwd_hash = b"$2b$12$uA/pjdOTD6exbOrMiyHE2OK2CM8vVoaflIRay8XU3E9YFWQorVSk2"

    assert Password.validate(pwd, pwd_hash)
