from __future__ import annotations
from src.models import Base

from sqlalchemy.sql.schema import ForeignKey as FK

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship as rel

from src.models.mercadoria import Mercadoria
from src.models.usuario import Usuario
from sqlalchemy import Integer

        
class Comuna(Base):
    
    __tablename__ = 'comuna'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # uuid
    # nome
    # sobre
    # data_de_criacao
    
    # postagens
    # usuarios
    # eventos
    # recursos_locais
    # votacao

    
