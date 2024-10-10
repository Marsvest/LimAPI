import socket
import asyncio

from RequestManager import request_manager


class Server:
    def __init__(self, host="127.0.0.1", port=8080) -> None:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)
        print(f"Сервер запущен на {host}:{port}")

    async def start_polling(self) -> None:
        while True:
            client_socket, addr = self.server_socket.accept()
            request = client_socket.recv(1024).decode()

            request_manager.process(request)

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
