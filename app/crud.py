from app.models import RegistroFoco

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

def get_registros(db):
    registros = db.query(RegistroFoco).all()

    return registros
 