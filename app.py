from sqlalchemy.orm import Session
from src.models import engine
from typing import List, Tuple, Optional, Callable
from pprint import pprint

from src import popular_o_banco_de_dados

popular_o_banco_de_dados()

from src.models import (
    Usuario,
    Mercadoria,
    Pedido,
    Correspondencia,
    Oferta,
    Demanda
)

def usuarios_nao_atendidos(
        usuarios_pedidos: List[int],
        correspondencias: List[Correspondencia]
    ) -> Tuple[List[int], List[int]]:
    correspondencias_usuarios_demanda = [
        correspondencia.demanda_id for correspondencia in correspondencias
    ]
    
    nao_atendidos_demanda: List[int] = []
    nao_atendidos_oferta: List[int] = []

    for usuario_id in correspondencias_usuarios_demanda:
        if usuario_id not in usuarios_pedidos:
            nao_atendidos_demanda.append(usuario_id)
    
    correspondencias_usuarios_oferta = [
        correspondencia.oferta_id for correspondencia in correspondencias
    ]
    for usuario_id in correspondencias_usuarios_oferta:
        if usuario_id not in usuarios_pedidos:
            correspondencias_usuarios_oferta.append(usuario_id)
            
    return nao_atendidos_demanda, nao_atendidos_oferta


def encadear(pedidos: List[Pedido]) -> List[Correspondencia]:
    
    ofertas: List[Oferta] = []
    demandas: List[Demanda] = []
    
    for pedido in pedidos:
        oferta = session.query(Oferta).filter_by(id=pedido.oferta_id).first()
        demanda = session.query(Demanda).filter_by(id=pedido.demanda_id).first()
        
        ofertas.append(oferta)
        demandas.append(demanda)

    correspondencias = []
    
    for oferta in ofertas:
        for demanda in demandas:
            
            if (oferta.produto_id == demanda.produto_id and
                oferta.usuario_id != demanda.usuario_id):
               
                correspondencias.append(Correspondencia(
                    oferta_id=oferta.id,
                    demanda_id=demanda.id,
                    pontuacao=0
                ))
                
    usuarios_ofertas = [oferta.usuario_id for oferta in ofertas]
    usuarios_demandas = [demanda.usuario_id for demanda in demandas]
    
    nao_atendidos_de, nao_atendidos_para = usuarios_nao_atendidos(
        usuarios_pedidos=usuarios_ofertas + usuarios_demandas,
        correspondencias=correspondencias
    )
    
    if nao_atendidos_de or nao_atendidos_para:
        msg = 'Usuarios não inclusos! De: {}, Para: {}'.format(
            str(nao_atendidos_de), str(nao_atendidos_para)
        )

        raise RuntimeError(msg)
    
    return correspondencias


with Session(engine) as session:
    pedidos = session.query(Pedido).all()
      
    transacoes = encadear(pedidos=pedidos)
    
    pprint(transacoes)
