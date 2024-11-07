# import asyncio
from LimAPI.Core import Server, Router
from LimAPI.Types import Request, Response


server = Server()


@Router.get("/")
async def main():
    # return "Hello, world!"
    response = Response(payload="1212")
    return response


@Router.get("/echo")
async def echo(text: str):
    return text


@Router.post("/test")
async def test(request: Request):
    print(request.cookie)
    # await asyncio.sleep(5)
    print("Выполнение полезной нагрузки...")
    return Response(payload="Test Success!")


server.run()
