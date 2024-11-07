from typing import Callable, Dict, Any, Tuple, Optional

from Core.Types import Request
from Core.utils import has_request


class EndpointManager:
    endpoints: Dict[str, Tuple[str, Callable]] = {}

    @classmethod
    def get(cls, route: str) -> Callable:
        return cls.create(route, "GET")

    @classmethod
    def post(cls, route: str) -> Callable:
        return cls.create(route, "POST")

    @classmethod
    def update(cls, route: str) -> Callable:
        return cls.create(route, "UPDATE")

    @classmethod
    def delete(cls, route: str) -> Callable:
        return cls.create(route, "DELETE")

    @classmethod
    def create(cls, route: str, method: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            cls.endpoints[route] = (method, func)
            return func

        return decorator

    @classmethod
    async def process(cls, request: Request) -> Optional[Tuple[str, Any]]:
        route: str = request.endpoint
        data = cls.endpoints.get(route)

        if data:
            method, bound_function = data
            if method == request.method:
                if has_request(bound_function):
                    response_data: Any = await bound_function(
                        request, **request.query_params
                    )
                else:
                    response_data: Any = await bound_function(**request.query_params)
                return method, response_data

        return None
