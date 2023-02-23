from src import models
from src.models import engine
from sqlalchemy.orm import Session


def criar_usuarios():
    from src.models import Usuario
    with Session(engine) as session:
        usuario = session.query(Usuario).first()
        if not usuario:
            usuarios = [
                Usuario(nome='padeiro'),
                Usuario(nome='açougueiro'),
                Usuario(nome='pizzaiolo'),
                Usuario(nome='agricultor')
            ]
            for usuario in usuarios:
                session.add(usuario)
                session.commit()

def criar_mercadorias():
    from src.models import Mercadoria
    with Session(engine) as session:
        mercadoria = session.query(Mercadoria).first()
        if not mercadoria:
            mercadorias = [
                Mercadoria(id=1,nome='pão', descricao='pão', categoria=1),
                Mercadoria(id=2,nome='carne', descricao='carne', categoria=1),
                Mercadoria(id=3,nome='pizza', descricao='pizza', categoria=1),
                Mercadoria(id=4,nome='frutas', descricao='frutas', categoria=1),
            ]
            for mercadoria in mercadorias:
                session.add(mercadoria)
                session.commit() 

def criar_ofertas():
    from src.models import Oferta
    with Session(engine) as session:
        oferta = session.query(Oferta).first()
        if not oferta:
            ofertas = [
                Oferta(id=1, usuario_id=1, produto_id=1),
                Oferta(id=2, usuario_id=2, produto_id=2),
                Oferta(id=3, usuario_id=3, produto_id=3),
                Oferta(id=4, usuario_id=4, produto_id=4),
            ]
            for oferta in ofertas:
                session.add(oferta)
                session.commit()
                
def criar_demandas():
    from src.models import Demanda
    with Session(engine) as session:
        demanda = session.query(Demanda).first()
        if not demanda:
            demandas = [
                Demanda(id=1, usuario_id=1, produto_id=2),
                Demanda(id=2, usuario_id=2, produto_id=3),
                Demanda(id=3, usuario_id=3, produto_id=4),
                Demanda(id=4, usuario_id=4, produto_id=1),
            ]
            for demanda in demandas:
                session.add(demanda)
                session.commit()
    
def criar_pedidos():
    from src.models import Pedido
    with Session(engine) as session:
        pedido = session.query(Pedido).first()
        if not pedido:
            pedidos = [
                Pedido(oferta_id=1, demanda_id=2, usuario_id=1),
                Pedido(oferta_id=2, demanda_id=3, usuario_id=2),
                Pedido(oferta_id=3, demanda_id=4, usuario_id=3),
                Pedido(oferta_id=4, demanda_id=1, usuario_id=4),
            ]
            for pedido in pedidos:
                session.add(pedido)
                session.commit()
           
def popular_o_banco_de_dados():
    
    criar_usuarios()
    criar_mercadorias()
    criar_ofertas()
    criar_demandas()
    criar_pedidos()
