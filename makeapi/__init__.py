from textwrap import wrap
import uvicorn, asyncio
from .request import *
from .route import *
from typing import *
from .responses import *
from .event import Event, handle_lifespan, handle_type

__version__ = "2.0.0"


class MakeAPI:
    def __init__(self, name: str) -> None:
        self.endpoints = set()
        self.events = set()
        self.name = name

    def event(self, event_name: str):
        def wrapper(f: typing.Callable):
            self.events.add(Event(event_name, f))

        return wrapper

    def get(self, path: str):
        def wrapper(f: typing.Callable):
            if not asyncio.iscoroutinefunction(f):
                raise RuntimeError(f"Function {f.__name__} is not a coroutine")
            self.endpoints.add(Route(path, f, "GET"))

        return wrapper

    def post(self, path: str):
        def wrapper(f: typing.Callable):
            if not asyncio.iscoroutinefunction(f):
                raise RuntimeError(f"Function {f.__name__} is not a coroutine")
            self.endpoints.add(Route(path, f, "POST"))

        return wrapper

    def put(self, path: str):
        def wrapper(f: typing.Callable):
            if not asyncio.iscoroutinefunction(f):
                raise RuntimeError(f"Function {f.__name__} is not a coroutine")
            self.endpoints.add(Route(path, f, "PUT"))

        return wrapper

    async def __call__(self, scope, receive, send):
        scope["app"] = self
        await handle_lifespan(scope, receive, send)
        await handle_type(scope, receive, send)
        req: Request = Request(scope)
        for endpoint in self.endpoints:
            endpoint: Route = endpoint
            if endpoint.path == req.path:
                if str(scope["method"]).lower() == endpoint.method.lower():
                    resp = await endpoint.callback(request=req)
                    await resp(scope, receive, send)
