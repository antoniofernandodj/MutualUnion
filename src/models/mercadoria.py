from __future__ import annotations
from src.models import Base

from sqlalchemy.sql.sqltypes import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, Text

    
class Mercadoria(Base):
    
    __tablename__ = 'mercadoria'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(100))
    descricao: Mapped[str] = mapped_column(Text)
    categoria: Mapped[int] = mapped_column(Integer) # 1 para mercadoria, 0 para serviço 
