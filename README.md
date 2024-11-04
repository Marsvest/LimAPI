![logo](https://github.com/user-attachments/assets/136cf449-f3d3-4214-82fe-0cb8a56b0d8b)
# Легковесный асинхронный веб-фреймворк для создания API

## Основые особенности
- Простота работы с инструментом
- Настройка авторизации в две строчки
- Автопагинация

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