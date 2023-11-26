from pydantic import  BaseModel


class AcessToken(BaseModel):
    access_token: str
    token_type: str


class AcessTokenData(BaseModel):
    username: str | None = None
    Role: list[str] = []
    Permission: list[str] = []
