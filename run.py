# import asyncio
from LimAPI.Core import Server, Router
from LimAPI.Types import Request


server = Server()


@Router.create("/")
async def main():
    return "Hello, world!"


@Router.create("/test")
async def test(request: Request):
    print(request.headers)
    # await asyncio.sleep(5)
    print('Выполнение полезной нагрузки...')
    return "Test Success!"


server.run()
