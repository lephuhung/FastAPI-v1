from pydantic import  BaseModel


class AccessToken(BaseModel):
    access_token: str
    token_type: str


class AccessTokenData(BaseModel):
    id: int
    username: str | None = None
    role: list[str] = []
    permission: list[str] = []