import asyncio
from asyncio import StreamReader, StreamWriter
from typing import Any

from Core.RequestManager import RequestManager
from Core.EndpointManager import EndpointManager
from Core.ResponseManager import ResponseManager
from Core.Types import Request


class Server:
    def __init__(self, host: str = "127.0.0.1", port: int = 8080) -> None:
        """Создание сервера

        Args:
            host (str): Хост сервера. Defaults to "127.0.0.1".
            port (int): Порт сервера. Defaults to 8080.
        """
        self.host = host
        self.port = port

    async def handle_request(self, reader: StreamReader, writer: StreamWriter) -> None:
        # Получение "сырого" запроса
        raw_request: bytearray = await reader.read(1024)

        # Обработка запроса
        request: Request = await RequestManager.process(raw_request.decode())

        # Роутинг запроса
        endpoint_data: Any = await EndpointManager.process(request)

        # Обработка ответа
        response: str = await ResponseManager.process(endpoint_data)

        # Заглушка
        response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"

        # Отправка ответа
        writer.write(response.encode())
        await writer.drain()
        writer.close()

    async def start_polling(self) -> None:
        """Асинхронный старт сервера"""
        server = await asyncio.start_server(self.handle_request, self.host, self.port)
        print(f"Сервер запущен на {self.host}:{self.port}")

        async with server:
            await server.serve_forever()

    def run(self) -> None:
        # TODO: Добавить try except Exception as e: print(e)
        asyncio.run(self.start_polling())
