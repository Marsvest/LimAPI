from typing import Callable, Dict, Any, Tuple

from Core.Types import Request
from Core.utils import has_request


class EndpointManager:
    endpoints: Dict[str, Tuple[str, Callable]] = {}

    @classmethod
    def get(self, route: str) -> Callable:
        return self.create(route, "GET")

    @classmethod
    def post(self, route: str) -> Callable:
        return self.create(route, "POST")

    @classmethod
    def update(self, route: str) -> Callable:
        return self.create(route, "UPDATE")

    @classmethod
    def delete(self, route: str) -> Callable:
        return self.create(route, "DELETE")

    @classmethod
    def create(self, route: str, method: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.endpoints[route] = method, func
            return func

        return decorator

    @classmethod
    async def process(self, request: Request) -> Tuple[str, Any]:
        route: str = request.endpoint
        data = self.endpoints.get(route)

        if data:
            method, bound_function = data
            if method == request.method:
                if has_request(bound_function):
                    response_data: Any = await bound_function(request)
                else:
                    response_data: Any = await bound_function()

                return method, response_data

        return None
