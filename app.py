from sqlalchemy.orm import Session
from src.models import engine
from typing import List, Tuple, Optional, Callable
from pprint import pprint
import networkx as nx
import matplotlib.pyplot as plt

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

def encontrar_correspondencias(pedidos: List[Pedido]) -> List[Correspondencia]:
    
    ofertas: List[Oferta] = []
    demandas: List[Demanda] = []
    
    with Session(engine) as session:
        
        for pedido in pedidos:
            oferta = session.query(Oferta).filter_by(id=pedido.oferta_id).first()
            demanda = session.query(Demanda).filter_by(id=pedido.demanda_id).first()
            
            ofertas.append(oferta)
            demandas.append(demanda)
            
        G = nx.DiGraph()
        
        for pedido in pedidos:
            G.add_node(pedido.id)
        
        for node_a in G.nodes:
            pedido1: Pedido = session.query(Pedido).filter_by(id=node_a).first()
            for node_b in G.nodes:
                if node_a != node_b:
                    pedido2: Pedido = session.query(Pedido).filter_by(id=node_b).first()
   
                    if ( pedido1.oferta.produto.id == pedido2.demanda.produto.id and
                        pedido1.usuario_id != pedido2.usuario_id):
                        
                        G.add_edge(
                            u_of_edge=pedido1.id,
                            v_of_edge=pedido2.id
                        )

        correspondencias = []
        for pedido_oferta_id, pedido_demanda_id in G.edges():

            pedido_oferta = session.query(Pedido).filter_by(id=pedido_oferta_id).first()
            pedido_demanda = session.query(Pedido).filter_by(id=pedido_demanda_id).first()

            correspondencia = Correspondencia(
                oferta_id=pedido_oferta.oferta.id,
                demanda_id=pedido_demanda.demanda.id,
                pontuacao=0
            )
            correspondencias.append(correspondencia)
        
        usuarios_ofertas = [oferta.usuario_id for oferta in ofertas]
        usuarios_demandas = [demanda.usuario_id for demanda in demandas]
        
        nao_atendidos_de, nao_atendidos_para = usuarios_nao_atendidos(
            usuarios_pedidos=usuarios_ofertas + usuarios_demandas,
            correspondencias=correspondencias
        )
        
        if nao_atendidos_de or nao_atendidos_para:
            raise RuntimeError('Usuarios não inclusos! De: {}, Para: {}'.format(
                str(nao_atendidos_de), str(nao_atendidos_para)
            ))
        else:
            print("Correspondencias válidas")
        
        
        return correspondencias

with Session(engine) as session:
    
    pedidos = session.query(Pedido).all()
    correspondencias = encontrar_correspondencias(pedidos=pedidos)
    print(correspondencias)
