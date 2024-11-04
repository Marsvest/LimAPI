from typing import Callable, Dict, Any

from Core.Types import Request


class EndpointManager:
    endpoints: Dict[str, Callable] = {}

    @classmethod
    def create(self, route: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.endpoints[route] = func
            return func

        return decorator

    @classmethod
    async def process(self, request: Request) -> Any:
        route: str = request.endpoint
        bound_function: Callable = self.endpoints.get(route)

        if bound_function:
            response_data: Any = await bound_function()
        else:
            return None

        return response_data
