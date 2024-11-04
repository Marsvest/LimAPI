from LimAPI import Server, Router


server = Server()


@Router.create("/")
async def main():
    return "Hello, world!"


@Router.create("/test")
async def test():
    print('Выполнение полезной нагрузки...')
    return "Test Success!"


server.run()
