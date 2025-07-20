from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Veiculo
from schemas import VeiculoSchema

engine = create_engine("sqlite:///db.sqlite")
Session = sessionmaker(bind=engine)


def buscar_veiculos(filtros: dict) -> List[dict]:
    session = Session()
    query = session.query(Veiculo)

    # consultar banco de dados e retornar lista de dict
    if "marca" in filtros and filtros["marca"]:
        query = query.filter(Veiculo.marca.in_(filtros["marca"]))
    if "modelo" in filtros and filtros["modelo"]:
        query = query.filter(Veiculo.modelo == filtros["modelo"])
    if "preco_max" in filtros and filtros["preco_max"]:
        query = query.filter(Veiculo.preco <= filtros["preco_max"])
    if "tipo" in filtros and filtros["tipo"]:
        query = query.filter(Veiculo.tipo == filtros["tipo"])
    if "combustivel" in filtros and filtros["combustivel"]:
        query = query.filter(Veiculo.combustivel == filtros["combustivel"])
    if "cor" in filtros and filtros["cor"]:
        query = query.filter(Veiculo.cor == filtros["cor"])
    if "ano_min" in filtros and filtros["ano_min"]:
        query = query.filter(Veiculo.ano >= filtros["ano_min"])
    if "km_max" in filtros and filtros["km_max"]:
        query = query.filter(Veiculo.km <= filtros["km_max"])
    if "transmissao" in filtros and filtros["transmissao"]:
        query = query.filter(Veiculo.transmissao == filtros["transmissao"])
    if "portas" in filtros and filtros["portas"]:
        query = query.filter(Veiculo.portas == filtros["portas"])

    return [VeiculoSchema.model_validate(v).model_dump() for v in query.all()]
