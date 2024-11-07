from dataclasses import dataclass, field
from typing import Any, List, Optional


@dataclass
class Header:
    name: str
    value: str


@dataclass
class Request:
    method: str
    endpoint: str
    cookie: Optional[str] = None
    params: Optional[List[str]] = field(default_factory=list)
    payload: Optional[str] = None
    headers: Optional[List[Header]] = field(default_factory=list)


@dataclass
class Response:
    payload: Any
    status_code: int = 0
    method: str = "none"
    cookie: Optional[str] = None
    headers: Optional[List[Header]] = field(default_factory=list)
