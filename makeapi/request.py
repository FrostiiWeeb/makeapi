import uvicorn
from typing import *
from .methods import *
from .parse import DICT


class RequestServer(object):
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port


class Request:
    def __init__(self, data: dict):
        self.request_type = data["type"]
        self.scheme = data["scheme"]
        self.root_path = data["root_path"]
        self.http_version = data["http_version"]
        self.method = (
            GET()
            if data["method"] == "GET"
            else POST()
            if data["method"] == "POST"
            else PATCH()
            if data["method"] == "PATCH"
            else PUT()
            if data["method"] == "PUT"
            else HEAD()
            if data["method"] == "HEAD"
            else None
        )
        self.path = data["path"]
        d_ = []
        for _name, _value in data["headers"]:
            name: bytes = _name
            value: bytes = _value
            d_.append([name.decode("utf-8"), value.decode("utf-8")])
        self.headers = DICT(d_)
        self.app = data["app"]
        data = data["server"]
        self.server = RequestServer(data[0], data[1])
