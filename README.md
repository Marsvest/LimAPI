![logo](https://github.com/user-attachments/assets/136cf449-f3d3-4214-82fe-0cb8a56b0d8b)
# Легковесный асинхронный веб-фреймворк для создания API

## Особенности фреймворка
- Простота, Гибкость, Скорость
- Настройка авторизации в две строчки (в разработке)
- Автопагинация (в разработке)

## Quickstart
```
from LimAPI.Core import Server, Router
from LimAPI.Types import Request


server = Server()


@Router.create("/")
async def main():
    return "Hello, world!"


@Router.create("/test")
async def test(request: Request):
    print(request.headers)
    print('Выполнение полезной нагрузки...')
    return "Test Success!"


server.run()

```