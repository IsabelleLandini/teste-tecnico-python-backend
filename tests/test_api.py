from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

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
        'comentario': 'teste'
    })
    
    assert response.status_code == 400

def test_diagnostico():
    response = client.get('/diagnostico-produtividade')

    assert response.status_code == 404
