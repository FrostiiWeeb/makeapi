from typing import *


class Route:
    def __init__(self, path: str, callback: Callable, method: str) -> None:
        self.path = path
        self.callback = callback
        self.method = method
