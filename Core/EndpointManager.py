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
                annotated_args = bound_function.__annotations__.keys()
                filtered_params = {
                    k: v for k, v in request.query_params.items() if k in annotated_args
                }

                try:
                    if has_request(bound_function):
                        response_data: Any = await bound_function(
                            request, **filtered_params
                        )
                    else:
                        response_data: Any = await bound_function(**filtered_params)
                    return method, response_data
                except Exception as e:
                    print(e)
                    return request.method, {"error": str(e)}

        return None
