import asyncio
from asyncio import StreamReader, StreamWriter

from Core.RequestManager import request_manager


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
        raw_request = await reader.read(1024)
        request = await request_manager.process(raw_request.decode())

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
        asyncio.run(self.start_polling())
