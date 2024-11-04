from dataclasses import dataclass


@dataclass
class Header:
    name: str
    value: str


@dataclass
class Request:
    method: str
    endpoint: str
    cookie: str | None
    payload: str | None
    headers: list[Header]
