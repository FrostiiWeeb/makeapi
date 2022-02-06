from makeapi import *
import uvicorn

api = MakeAPI(__name__)


@api.get("/")
async def index(request: Request):
    return Response("Hello World.")


uvicorn.run(api)
