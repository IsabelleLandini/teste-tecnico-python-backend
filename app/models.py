from sqlalchemy import Column, Integer, String
from app.database import Base

class RegistroFoco(Base):
    __tablename__ = 'registros_foco'

    id=Column(Integer, primary_key=True, index=True)
    nivel_foco=Column(Integer, nullable=False)
    tempo_minutos=Column(Integer, nullable=False)
    comentario=Column(String, nullable=False)
    categoria=Column(String)