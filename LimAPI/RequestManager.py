from Types import Request


class RequestManager:
    def __init__(self) -> None:
        pass

    def parse(self, raw_request: str) -> Request:
        headers: list[str] = raw_request.split("\r\n")
        print(headers)

    def process(self, request: Request | str):
        if type(request) is str:
            request = self.parse(request)


request_manager = RequestManager()
