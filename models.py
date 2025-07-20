from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Veiculo(Base):
    __tablename__ = "veiculos"

    id = Column(Integer, primary_key=True)
    marca = Column(String)
    modelo = Column(String)
    preco = Column(Float)
    tipo = Column(String)
    combustivel = Column(String)
    cor = Column(String)
    ano = Column(Integer)
    km = Column(Integer)
    transmissao = Column(String)
    portas = Column(Integer)
