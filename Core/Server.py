import asyncio
from asyncio import StreamReader, StreamWriter

from Core.RequestManager import RequestManager
from Core.EndpointManager import EndpointManager
from Core.ResponseManager import ResponseManager
from Core.Types import Request

from WatchDog.Watcher import Watcher


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
        data = await EndpointManager.process(request)
        if data:
            method, endpoint_data = data
            status_code: int = 201 if method == "POST" else 200
        else:
            method: str = "GET"
            endpoint_data = "Endpoint doesn't exists"
            status_code: int = 404

        # Обработка ответа
        response: str = await ResponseManager.process(
            method, status_code, endpoint_data
        )

        # Отправка ответа
        writer.write(response.encode())
        await writer.drain()
        writer.close()

    async def start_polling(self) -> None:
        """Асинхронный старт сервера"""
        server = await asyncio.start_server(self.handle_request, self.host, self.port)
        print(f"Сервер запущен на {self.host}:{self.port}")

        async with server:
            await Watcher.watch()
            await server.serve_forever()

    def run(self) -> None:
        try:
            asyncio.run(self.start_polling())
        except Exception as e:
            print(e)
