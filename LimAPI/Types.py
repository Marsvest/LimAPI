from pydantic import BaseModel

class Request(BaseModel):
    method: str