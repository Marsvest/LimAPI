import json
from typing import Any

from Core.Types import Response, Header


class ResponseManager:
    @classmethod
    async def process(
        self, method: str, status_code: int, data: Any | Response
    ) -> Response:
        if type(data) is Response:
            data.method = method if not data.method else data.method
            data.status_code = status_code if not data.status_code else data.status_code
            response: Response = await self.add_require_fields(data)
        else:
            response: Response = await self.add_require_fields(
                Response(method=method, payload=data, status_code=status_code)
            )

        cooked_response: str = await self.stringify(response)

        return cooked_response

    @classmethod
    async def add_require_fields(self, response: Response) -> Response:
        if not [header.name == "Content-Type" for header in response.headers]:
            if type(response.payload) is dict:
                response.headers.append(
                    Header(name="Content-Type", value="application/json")
                )
                response.payload = json.dumps(response.payload)
            else:
                response.headers.append(Header(name="Content-Type", value="text/plain"))

            # TODO: обработка остальных типов данных
            return response

    @classmethod
    async def stringify(self, response: Response) -> str:
        ok_or_error: str = "OK" if response.status_code in range(200, 400) else "ERROR"
        result: str = f"HTTP/1.1 {response.status_code} {ok_or_error}\r\n"

        for header in response.headers:
            result += f"{header.name}: {header.value}\r\n"

        if response.cookie:
            result += f"Set-Cookie: {response.cookie}\r\n"

        result += "\r\n"
        result += str(response.payload)

        return result
