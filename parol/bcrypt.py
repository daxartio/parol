from typing import NamedTuple

import bcrypt


class Password(NamedTuple):
    password: bytes

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return "Password(password='***')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Password):  # pragma:no cover
            return NotImplemented
        return self.password == other.password

    def hash(self, rounds: int = 12) -> bytes:  # noqa:A003
        return bcrypt.hashpw(self.password, bcrypt.gensalt(rounds))

    @staticmethod
    def validate(
        password: bytes,
        hash: bytes,  # noqa:A002 pylint:disable=redefined-builtin
    ) -> bool:
        return bcrypt.checkpw(password, hash)
