from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app.schemas import RegistroFocoCreate
from app.crud import create_registro_foco, get_registros

app = FastAPI(
    title= "Log de Performance API",
    description= (
        "API para registro de sessões de foco e produtividade, "
        "gerando um diagnóstico sobre o desempenho do usuário "
        "durante seu período de trabalho ou estudo."
    ),
    version="1.0.0",
    contact={
        "name": "Isabelle Landini",
        "email": "isa_landini@hotmail.com"
    },
    docs_url='/docs',
    redoc_url='/redoc' 
)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home():
    return {'message': 'Log de Performance API funcionando com sucesso.'}

@app.post('/registro-foco', status_code=201)
def post_registro(
    registro: RegistroFocoCreate,
    db: Session = Depends(get_db)
):
    return create_registro_foco(db, registro)

@app.get('/diagnostico-produtividade')
def get_registro(
    db:Session = Depends(get_db)
):
    registros = get_registros(db)
    if not registros:
        return {'message': 'Nenhum registro encontrado.'}

    media_foco = sum(registro.nivel_foco for registro in registros) / len(registros)
    
    tempo_total = sum(registro.tempo_minutos for registro in registros)

    if media_foco < 3:
        feedback = 'Pausas mais longas e menos notificações podem ajudar.'
    elif media_foco <= 4:
        feedback = 'Seu foco está bom, mas ainda há espaço para melhorar.' 
    else:
        feedback = 'Você está em uma maratona produtiva de alto nível!'
    
    return {
        'media_nivel_foco': media_foco,
        'tempo_total_focado': tempo_total,
        'feedback': feedback
    }