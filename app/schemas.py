from pydantic import BaseModel, Field
from typing import Optional

class RegistroFocoCreate(BaseModel):
    nivel_foco: int = Field(..., ge=1, le=5)
    tempo_minutos: int = Field(..., gt=0)
    comentario: str
    categoria: Optional[str] = None