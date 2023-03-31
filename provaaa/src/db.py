from sqlalchemy import create_engine
from models.base import Base
from sqlalchemy.orm import Session, sessionmaker
from models.jogos import Jogos


engine = create_engine("sqlite:///db.py", echo=True, future=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)


dead = Jogos(
    name="Dead Space Remake",
    plataforma="PS5",
    preco="350",
    quantidade="10",
     )
Forspoken = Jogos(
    name="Forspoken",
    plataforma="PC",
    preco="299",
    quantidade="8",
     )
Deadisland = Jogos(
    name="Dead island",
    plataforma="PS5",
    preco="350",
    quantidade="10",
     )
Hogwarts = Jogos(
    name="Hogwarts Legacy",
    plataforma="PC",
    preco="219",
    quantidade="7",
     )
wild = Jogos(
    name="Wild Hearts",
    plataforma="Xbox Series",
    preco="350",
    quantidade="7",
     )
re = Jogos(
    name="resisdent evil 4(melhor jogo da história)",
    plataforma="PS5",
    preco="289",
    quantidade="10",
     )

zelda = Jogos(
    name="The Legend Of Zelda",
    plataforma="Switch",
    preco="350",
    quantidade="10",
     )
session.add_all([dead, Forspoken, Deadisland, Hogwarts, wild, re, zelda])

session.commit()

