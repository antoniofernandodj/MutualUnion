from src.models import Usuario, Transacao, engine
from sqlalchemy.orm import Session

def calcular_distancia(de, para):
    return 0

def preferencia_distancia(transacao: Transacao) -> int:
    with Session(engine) as session:
        de = session.query(Usuario).filter_by(id=transacao.de_id).first()
        para = session.query(Usuario).filter_by(id=transacao.para_id).first()
        # Usar uma API de mapas para calcular a distância entre de e para
        distancia = calcular_distancia(de.cep, para.cep)
        return -distancia  # Retornar negativo para ordenar por distância crescente