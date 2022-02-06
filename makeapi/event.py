import typing


class Event:
    def __init__(self, name: str, callback: typing.Callable) -> None:
        self.name = name
        self.callback = callback

    async def __call__(self):
        return await self.callback()


async def handle_lifespan(scope, receive, send):
    if scope["type"] == "lifespan":
        while True:
            message = await receive()
            if message["type"] == "lifespan.startup":
                for event in scope["app"].events:
                    event: Event = event
                    if event.name == "on_start":
                        await event()
                await send({"type": "lifespan.startup.complete"})
            elif message["type"] == "lifespan.shutdown":
                for event in scope["app"].events:
                    event: Event = event
                    if event.name == "on_stop":
                        await event()
                await send({"type": "lifespan.shutdown.complete"})
                return


async def handle_type(scope, receive, send):
    if scope["type"] != "http":
        raise RuntimeError("Request type is not HTTP. Ignoring..")
