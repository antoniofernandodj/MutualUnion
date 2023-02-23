from __future__ import annotations
from src.models import Base, Usuario, Mercadoria, Oferta, Demanda

from sqlalchemy.sql.schema import ForeignKey as FK

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship as rel


from sqlalchemy import Integer

        
class Correspondencia(Base):
    
    __tablename__ = 'correspondencia'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    
    demanda_id: Mapped[int] = mapped_column(FK("demanda.id"))
    demanda: Mapped[Demanda] = rel(Demanda, backref="demandas", foreign_keys=[demanda_id])
    
    oferta_id: Mapped[int] = mapped_column(FK("oferta.id"))
    oferta: Mapped[Oferta] = rel(Oferta, backref="ofertas", foreign_keys=[oferta_id])
    
    pontuacao: Mapped[int] = mapped_column(Integer, nullable=True)
    
    def __repr__(self):
        
        return 'Correspondencia {{ oferta_id:{}, demanda_id:{}, pont: {} }}'.format(
            self.oferta_id, self.demanda_id, self.pontuacao
        )

    def __str__(self):
        
        return 'Correspondencia {{ oferta_id:{}, demanda_id:{}, pont: {} }}'.format(
            self.oferta_id, self.demanda_id, self.pontuacao
        )
