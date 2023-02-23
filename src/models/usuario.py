from __future__ import annotations
from src.models import Base

from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import String

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer


class Usuario(Base):
    
    __tablename__ = 'usuario'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # postagens
    
    nome: Mapped[str] = mapped_column(String(100))
    cpf: Mapped[str] = mapped_column(String(100), nullable=True)
    cep: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    telefone: Mapped[str] = mapped_column(String(100), nullable=True)
    celular: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    site: Mapped[str] = mapped_column(String(100), nullable=True)
