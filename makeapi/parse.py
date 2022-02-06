from yarl import URL
import typing


class DICT(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get(self, name: str):
        return self.__getattribute__(name)

    def __getattribute__(self, __name: str) -> typing.Any:
        return super().__getattribute__(__name.lower())
