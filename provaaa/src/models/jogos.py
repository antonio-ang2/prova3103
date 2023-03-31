from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from models.base import Base


class Jogos(Base):
     __tablename__ = "jogoes"

     id = Column(Integer, primary_key=True)
     nome = Column(String)
     plataforma = Column(String)
     preco = Column(String)
     quantidade = Column(Integer)

     def __repr__(self):
         return f"Jogos(id={self.id!r}, nome={self.nome!r}, plataforma={self.plataforma!r}), preco={self.preco!r},quantidade={self.quantidade!r}"