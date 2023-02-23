from __future__ import annotations
from src.models import Base

from sqlalchemy.sql.schema import ForeignKey as FK

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship as rel

from src.models.mercadoria import Mercadoria
from src.models.usuario import Usuario
from sqlalchemy import Integer

        
class Pedido(Base):
    
    __tablename__ = 'pedido'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    oferta_id: Mapped[int] = mapped_column(FK("mercadoria.id"))
    oferta: Mapped[Mercadoria] = rel(Mercadoria, backref="oferta", foreign_keys=[oferta_id])
    
    usuario_id: Mapped[int] = mapped_column(FK("usuario.id"))
    usuario: Mapped[Mercadoria] = rel(Usuario, backref="usuarios", foreign_keys=[usuario_id])
    
    demanda_id: Mapped[int] = mapped_column(FK("mercadoria.id"))
    demanda: Mapped[Mercadoria] = rel(Mercadoria, backref="demanda", foreign_keys=[demanda_id])
    
    def __repr__(self):
        return f'Pedido {{ oferta:{self.oferta_id}, demanda:{self.demanda_id} }}'
    
