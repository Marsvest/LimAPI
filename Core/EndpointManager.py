from typing import Callable, Dict, Any


class EndpointManager:
    endpoints: Dict[str, Callable[..., Any]] = {}

    @classmethod
    def create(cls, route: str) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            cls.endpoints[route] = func
            return func

        return decorator
