from typing import Any

from Core.Types import Response


class ResponseManager:
    @classmethod
    async def process(self, data: Any | Response) -> Response:
        if type(data) is Response:
            response: Response = await self.add_require_fields(data)
        else:
            response: Response = await self.create_from_empty(data)

        cooked_response: str = await self.stringify(response)

        return cooked_response

    @classmethod
    async def add_require_fields(self, response: Response) -> Response:
        pass

    @classmethod
    async def create_from_empty(self, data: Any) -> Response:
        pass

    @classmethod
    async def stringify(self, response: Response) -> str:
        pass
