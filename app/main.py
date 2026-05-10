from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app.schemas import RegistroFocoCreate, DiagnosticoResponse
from app.crud import create_registro_foco, get_registros
from app.services import calcular_diagnostico 


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

# Criação de tabelas no banco caso ainda não existam
Base.metadata.create_all(bind=engine)

def get_db():
    # Cria uma sessão de banco de dados para cada requisição
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home():
    return {'message': 'Log de Performance API funcionando com sucesso.'}

# Endpoint responsável por registrar uma nova sessão de foco do usuário
@app.post('/registro-foco', status_code=201)
def post_registro(
    registro: RegistroFocoCreate,
    db: Session = Depends(get_db)
):
    # Garantindo que o nível de foco esteja dentro do intervalo permitido
    if registro.nivel_foco < 1 or registro.nivel_foco > 5:
        raise HTTPException(
            status_code=400,
            detail='nivel_foco deve estar entre 1 e 5')
    if registro.tempo_minutos <= 0:
        raise HTTPException(
            status_code=400,
            detail='tempo_minutos deve ser maior que 0')
    
    return create_registro_foco(db, registro)

# Busca todos os registros para gerar análise de produtividade
@app.get(
        '/diagnostico-produtividade', 
        response_model=DiagnosticoResponse, # garante padronização da resposta da API 
        status_code=200
    )
def get_diagnostico_produtividade(db:Session = Depends(get_db)):
    registros = get_registros(db)
    # Se não houver dados, retorna erro controlado
    if not registros:
        raise HTTPException(
            status_code=404,
            detail= 'Nenhum registro encontrado.'
        )
    # Delega a lógica de cálculo para a camada de service
    return calcular_diagnostico(registros)
    