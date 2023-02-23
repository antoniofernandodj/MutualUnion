from __future__ import annotations
from sqlalchemy.engine.create import create_engine
from sqlalchemy.orm import declarative_base

from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase): pass

Base = declarative_base()

DATABASE_URL = 'sqlite:///database.sqlite3'
engine = create_engine(url=DATABASE_URL)

from src.models.usuario import Usuario
from src.models.mercadoria import Mercadoria
from src.models.oferta import Oferta
from src.models.demanda import Demanda
from src.models.pedido import Pedido
from src.models.correspondencia import Correspondencia

Base.metadata.create_all(engine)
