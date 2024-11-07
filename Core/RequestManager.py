import json
from urllib.parse import parse_qs

from Core.Types import Request, Header
from Core.utils import clean_array


class RequestManager:
    @classmethod
    async def parse(cls, raw_request: str) -> Request:
        """Создание типизированного объекта запроса

        Args:
            raw_request (str): Строка запроса

        Returns:
            Request: Объект запроса
        """
        raw_headers: list[str] = clean_array(raw_request.split("\r\n"))

        headers: list[Header] = []
        body: list[str] = [""]
        method = endpoint = ""
        query_params = {}

        for raw_header in raw_headers:
            if "HTTP" in raw_header:
                method, endpoint_with_query = raw_header.split(" /")
                endpoint_with_query, _ = endpoint_with_query.split(" ")
                endpoint, query_str = (
                    endpoint_with_query.split("?", 1)
                    if "?" in endpoint_with_query
                    else (endpoint_with_query, "")
                )
                query_params = parse_qs(query_str)
                continue
            elif raw_header == "{":
                body = raw_headers[raw_headers.index(raw_header) :]
                break
            else:
                name, value = raw_header.split(": ", 1)
                headers.append(Header(name=name, value=value))

        body_str = "".join([elem.strip() for elem in body])

        request = Request(
            method=method,
            endpoint="/" + endpoint,
            cookie=next(
                (header.value for header in headers if header.name == "Cookie"), None
            ),
            payload=json.loads(body_str) if body_str else {},
            headers=headers,
            query_params=query_params,
        )

        return request

    @classmethod
    async def process(cls, request: Request | str) -> Request:
        if isinstance(request, str):
            request = await cls.parse(request)

        return request
