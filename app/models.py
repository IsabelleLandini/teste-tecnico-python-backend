from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, UTC

from app.database import Base

# Tabela principal que armazena sessões de foco do usuário
class RegistroFoco(Base):
    __tablename__ = 'registros_foco'

    id=Column(Integer, primary_key=True, index=True)
    nivel_foco=Column(Integer, nullable=False)
    tempo_minutos=Column(Integer, nullable=False)
    comentario=Column(String, nullable=False)
    categoria=Column(String)
    data_registro = Column(DateTime, default=lambda: datetime.now(UTC))
    