import json
from typing import Any, Union
from Core.Types import Response, Header


class ResponseManager:
    @classmethod
    async def process(
        self, method: str, status_code: int, data: Union[Any, Response]
    ) -> str:
        response = (
            await self.add_required_fields(data)
            if isinstance(data, Response)
            else await self.add_required_fields(
                Response(method=method, payload=data, status_code=status_code)
            )
        )

        return await self.stringify(response)

    @classmethod
    async def add_required_fields(cls, response: Response) -> Response:
        if not any(header.name == "Content-Type" for header in response.headers):
            content_type = (
                "application/json"
                if isinstance(response.payload, dict)
                else "text/plain"
            )
            response.headers.append(Header(name="Content-Type", value=content_type))

            if isinstance(response.payload, dict):
                response.payload = json.dumps(response.payload)

        return response

    @classmethod
    async def stringify(cls, response: Response) -> str:
        status_text = "OK" if 200 <= response.status_code < 400 else "ERROR"
        result = f"HTTP/1.1 {response.status_code} {status_text}\r\n"

        result += "".join(
            f"{header.name}: {header.value}\r\n" for header in response.headers
        )

        if response.cookie:
            result += f"Set-Cookie: {response.cookie}\r\n"

        result += "\r\n" + str(response.payload)

        return result
