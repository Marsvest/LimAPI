import socket
import asyncio


class Server:
    def __init__(self, host="127.0.0.1", port=8080) -> None:
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen(1)
        print(f"\nСервер запущен на {host}:{port}")

    async def main(self) -> None:
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Подключение от {addr}")

            request = client_socket.recv(1024).decode()
            print(f"Получен запрос:\n{request}")

            # Обработка GET-запроса
            if request.startswith("GET"):
                response = (
                    "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!"
                )
            else:
                response = "HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\n\r\n404 Not Found"

            client_socket.sendall(response.encode())
            client_socket.close()

    def run(self) -> None:
        asyncio.run(self.main())


if __name__ == "__main__":
    server = Server()
    server.run()
