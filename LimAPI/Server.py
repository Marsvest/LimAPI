import socket
import asyncio

from RequestManager import request_manager


class Server:
    def __init__(self, host: str = "127.0.0.1", port: int = 8080) -> None:
        """Создание сервера

        Args:
            host (str): Хост сервера. Defaults to "127.0.0.1".
            port (int): Порт сервера. Defaults to 8080.
        """
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)
        print(f"Сервер запущен на {host}:{port}")

    async def start_polling(self) -> None:
        """Асинхронный старт сервера"""
        while True:
            client_socket, addr = self.server_socket.accept()
            request = client_socket.recv(1024).decode()

            await request_manager.process(request)

            # Заглушка
            response = (
                "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
            )

            # TODO: Добавить обработку ответа Response
            client_socket.sendall(response.encode())
            client_socket.close()

    def run(self) -> None:
        asyncio.run(self.start_polling())


if __name__ == "__main__":
    server = Server()
    server.run()
