![logo](https://github.com/user-attachments/assets/136cf449-f3d3-4214-82fe-0cb8a56b0d8b)
# Легковесный асинхронный веб-фреймворк для создания API

## Особенности фреймворка
- Простота, Гибкость, Скорость
- Настройка авторизации в две строчки (в разработке)
- Автопагинация (в разработке)

## Quickstart
```
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

```