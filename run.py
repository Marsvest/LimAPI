from LimAPI import Server, Endpoint

server = Server()


@Endpoint.create("/")
async def main():
    return "Hello, world!"


@Endpoint.create("/test")
async def test():
    return "Test Success!"


server.run()
