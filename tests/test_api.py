import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import RegistroFoco
from app.database import SessionLocal

client = TestClient(app)

@pytest.fixture(autouse=True)
def limpar_db():
    db = SessionLocal()
    db.query(RegistroFoco).delete()
    db.commit()
    db.close()
    yield

def test_criar_registro():
    response = client.post('/registro-foco', json={
    'nivel_foco': 4,
    'tempo_minutos': 60,
    'comentario': 'Estudando FastAPI',
    'categoria': 'estudo'  
    })

    assert response.status_code == 201
    assert response.json()['nivel_foco'] == 4

def test_nivel_foco_invalido():
    response = client.post('/registro-foco', json={
        'nivel_foco': 10,
        'tempo_minutos': 60,
        'comentario': 'teste',
        'categoria': 'teste'
    })
    
    assert response.status_code == 400

def test_diagnostico_com_registro():
    client.post('/registro-foco', json={
        'nivel_foco': 4,
        'tempo_minutos': 60,
        'comentario': 'teste',
        'categoria': 'estudo'
    })

    response = client.get('/diagnostico-produtividade')

    assert response.status_code == 200
    assert 'media_foco' in response.json()
    assert 'feedback' in response.json()

def test_diagnostico_sem_registros():
    response = client.get('/diagnostico-produtividade')

    assert response.status_code == 404


