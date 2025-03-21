"""docString"""

from dotenv import load_dotenv
from typing import cast
from os import getenv

load_dotenv()
MESSAGE: str = cast(str, getenv("MESSAGE"))


class Main:
    """docString"""

    __slots__ = ("_msg",)

    def __init__(self, msg: str, /) -> None:
        """docString"""

        self.msg = msg

    @property
    def msg(self) -> str:
        """docString"""

        return self._msg

    @msg.setter
    def msg(self, value: str) -> None:
        """docString"""

        if not isinstance(value, str):
            raise TypeError("E: argument must be a string.")

        self._msg = value

    def echo(self) -> str:
        """docString"""

        return self._msg


if __name__ == "__main__":
    M = Main(MESSAGE)

    res: str = M.echo()
    print(res)
