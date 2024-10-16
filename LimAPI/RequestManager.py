import json
from Types import Request, Header
from utils import clean_array


class RequestManager:
    async def parse(self, raw_request: str) -> Request:
        """Создание типизированного объекта запроса

        Args:
            raw_request (str): Строка запроса

        Returns:
            Request: Объект запроса
        """
        raw_headers: list[str] = clean_array(raw_request.split("\r\n"))

        # Обработка хедеров
        headers: list[Header] = []
        body: str = ""

        for raw_header in raw_headers:
            if "HTTP" in raw_header:
                method, endpoint = raw_header.split(" /")
                continue
            elif raw_header == "{":
                body = raw_headers[raw_headers.index(raw_header) :]
                break
            else:
                name, value = raw_header.split(": ", 1)
                headers.append(Header(name=name, value=value))

        body_str = "".join([elem.strip(" ") for elem in body])

        # Создание запроса
        request = Request(
            method=method,
            endpoint=endpoint,
            cookie=next(
                (header.value for header in headers if header.name == "Cookie"), None
            ),
            payload=json.dumps(body_str),
            headers=headers,
        )

        return request

    async def process(self, request: Request | str) -> None:
        if type(request) is str:
            request = await self.parse(request)


request_manager = RequestManager()
