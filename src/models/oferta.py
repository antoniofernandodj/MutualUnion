from __future__ import annotations
from src.models import Base, Usuario, Mercadoria

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship as rel
from sqlalchemy.schema import ForeignKey as FK
from sqlalchemy import Integer

    
class Oferta(Base):
    
    __tablename__ = 'oferta'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    produto_id: Mapped[int] = mapped_column(FK("mercadoria.id"))
    produto: Mapped[Mercadoria] = rel(Mercadoria, backref="produtos", foreign_keys=[produto_id])
    
    usuario_id: Mapped[int] = mapped_column(FK("usuario.id"))
    usuario: Mapped[Mercadoria] = rel(Usuario, backref="ofertas", foreign_keys=[usuario_id])

    def __repr__(self):
        return f'Oferta {{ usuario_id:{self.usuario_id}, produto_id:{self.produto_id} }}'