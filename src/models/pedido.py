from __future__ import annotations
from src.models import Base, Usuario, Mercadoria, Oferta, Demanda

from sqlalchemy.sql.schema import ForeignKey as FK

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship as rel

from sqlalchemy import Integer

        
class Pedido(Base):
    
    __tablename__ = 'pedido'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    oferta_id: Mapped[int] = mapped_column(FK("oferta.id"))
    oferta: Mapped[Oferta] = rel(Oferta, backref="pedidos", foreign_keys=[oferta_id])
    
    usuario_id: Mapped[int] = mapped_column(FK("usuario.id"))
    usuario: Mapped[Mercadoria] = rel(Usuario, backref="pedidos", foreign_keys=[usuario_id])
    
    demanda_id: Mapped[int] = mapped_column(FK("demanda.id"))
    demanda: Mapped[Demanda] = rel(Demanda, backref="pedidos", foreign_keys=[demanda_id])
    
    def __repr__(self):
        return f'Pedido {{ oferta:{self.oferta_id}, demanda:{self.demanda_id} }}'
    
