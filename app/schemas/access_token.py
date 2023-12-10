from pydantic import  BaseModel, UUID4


class AccessToken(BaseModel):
    access_token: str
    token_type: str


class AccessTokenData(BaseModel):
    id: UUID4
    donvi_id: UUID4
    username: str | None = None
    role: list[str] =[]
    permission: list[str] = []