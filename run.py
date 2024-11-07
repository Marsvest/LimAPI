from LimAPI.Core import Server, Router
from LimAPI.Types import Request, Response


server = Server()


@Router.get("/echo")
async def echo(text: str):
    return text


@Router.get("/test")
async def test(request: Request):
    print(request.cookie)
    print("Выполнение полезной нагрузки...")
    return Response(payload="Test Success!", status_code=200)


server.run()
