from typing import *


class Response:
    def __init__(
        self,
        content: str,
        status_code: Optional[int] = 200,
        content_type: str = "text/plain",
    ) -> None:
        self.starting = {
            "type": "http.response.start",
            "status": status_code,
            "headers": [
                [b"content-type", content_type.encode()],
            ],
        }
        self.body = {
            "type": "http.response.body",
            "body": content.encode("utf-8"),
        }

    async def __call__(self, scope, receive, send) -> Any:
        await send(self.starting)
        return await send(self.body)
