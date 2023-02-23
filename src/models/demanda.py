from __future__ import annotations
from src.models import Base, Usuario, Mercadoria

from sqlalchemy.sql.sqltypes import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship as rel
from sqlalchemy.schema import ForeignKey as FK
from sqlalchemy import Integer

    
class Demanda(Base):
    
    __tablename__ = 'demanda'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    produto_id: Mapped[int] = mapped_column(FK("mercadoria.id"))
    produto: Mapped[Usuario] = rel(Mercadoria, backref="produtos_demanda", foreign_keys=[produto_id])

    usuario_id: Mapped[int] = mapped_column(FK("usuario.id"))
