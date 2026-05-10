from pydantic import BaseModel
from typing import Optional

class RegistroFocoCreate(BaseModel):
    nivel_foco: int
    tempo_minutos: int 
    comentario: str = ""
    categoria: Optional[str] = None

class DiagnosticoResponse(BaseModel):
    media_foco: float
    tempo_total_focado: int
    feedback: str
    