from pydantic import BaseModel
# from dataclasses import dataclass


class Header(BaseModel):
    name: str
    value: str


class Request(BaseModel):
    method: str
    endpoint: str
    cookie: str | None
    payload: str | None
    headers: list[Header]
