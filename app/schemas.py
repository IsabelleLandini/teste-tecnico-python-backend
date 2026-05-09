from pydantic import BaseModel
from typing import Optional

class RegistroFocoCreate(BaseModel):
    nivel_foco: int
    tempo_minutos: int 
    comentario: str = ""
    categoria: Optional[str] = None
