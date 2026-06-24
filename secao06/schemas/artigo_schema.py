from typing import Optional

from pydantic import BaseModel, HttpUrl

class ArtigoSchema(BaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int] = None

    class Config:
        orm_mode = True


class ArtigoPayloadSchema(BaseModel):
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    class Config:
        orm_mode = True

class ArtigoResponseSchema(ArtigoPayloadSchema):
    id: int
    usuario_id: int