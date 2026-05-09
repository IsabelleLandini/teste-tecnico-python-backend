from fastapi import FastAPI, Depends, HTTPException
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
    if registro.nivel_foco < 1 or registro.nivel_foco > 5:
        raise HTTPException(
            status_code=400,
            detail='nivel_foco deve estar entre 1 e 5')
    if registro.tempo_minutos <= 0:
        raise HTTPException(
            status_code=400,
            detail='tempo_minutos deve ser maior que 0')
    
    return create_registro_foco(db, registro)

@app.get('/diagnostico-produtividade', status_code=200)
def get_diagnostico_produtividade(
    db:Session = Depends(get_db)
):
    registros = get_registros(db)
    if not registros:
        raise HTTPException(
            status_code=404,
            detail= 'Nenhum registro encontrado.'
        )

    media_foco = sum(r.nivel_foco for r in registros) / len(registros)
    media_foco = round(media_foco, 2)
    
    tempo_total = sum(r.tempo_minutos for r in registros)

    if media_foco < 3:
        feedback = 'Pausas mais longas e menos notificações podem ajudar.'
    elif media_foco <= 4:
        feedback = 'Seu foco está bom, mas ainda há espaço para melhorar.' 
    else:
        feedback = 'Você está em uma maratona produtiva de alto nível!'
    
    return {
        'media_foco': round(media_foco,2),
        'tempo_total_focado': tempo_total,
        'feedback': feedback
    }