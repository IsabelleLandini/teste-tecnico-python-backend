from app.models import RegistroFoco

# Cria novo registro de foco no banco de dados
def create_registro_foco(db, registro):
    novo_registro = RegistroFoco(
        nivel_foco=registro.nivel_foco,
        tempo_minutos=registro.tempo_minutos,
        comentario=registro.comentario,
        categoria=registro.categoria
    )

    db.add(novo_registro)
    db.commit()
    db.refresh(novo_registro)

    return novo_registro

# Recuper todos os registros para cálculo de diagnóstico
def get_registros(db):
    registros = db.query(RegistroFoco).all()

    return registros
 