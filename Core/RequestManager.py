import json

from Core.Types import Request, Header
from Core.utils import clean_array


class RequestManager:
    @classmethod
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
        body: list[str] = [""]

        for raw_header in raw_headers:
            if "HTTP" in raw_header:
                method, endpoint = raw_header.split(" /")
                endpoint, _ = endpoint.split(" ")
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

    @classmethod
    async def process(self, request: Request | str) -> Request:
        if type(request) is str:
            request = await self.parse(request)

        return request
