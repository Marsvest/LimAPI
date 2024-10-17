![logo](https://github.com/user-attachments/assets/136cf449-f3d3-4214-82fe-0cb8a56b0d8b)
# Легковесный асинхронный веб-фреймворк для создания API

## Основые особенности
- Простота работы с инструментом
- Настройка авторизации в две строчки
- Автопагинация

## Quickstart
```
from LimAPI import Server


app = Server()


@app.get("/")
async def main():
   return "Hello world!"


app.run()
```