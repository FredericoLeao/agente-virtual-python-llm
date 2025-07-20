import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Veiculo

engine = create_engine("sqlite:///db.sqlite")
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

MARCAS_MODELOS = {
    "Fiat": ["Uno", "Argo", "Mobi"],
    "Chevrolet": ["Onix", "Prisma", "Corsa"],
    "Volkswagen": ["Gol", "Fox", "Polo"],
    "Toyota": ["Corolla", "Etios", "Yaris"],
    "Ford": ["Ka", "Fiesta", "Focus"],
    "Honda": ["Civic", "Fit", "City"],
    "Hyundai": ["HB20", "Creta"],
    "Renault": ["Sandero", "Logan", "Kwid"],
}

TIPOS = ["hatch", "sedan", "SUV", "pickup"]
COMBUSTIVEIS = ["gasolina", "etanol", "flex", "diesel"]
CORES = ["preto", "branco", "prata", "vermelho", "azul", "cinza"]

DADOS_VEICULOS = []

for _ in range(200):
    v = Veiculo(
        marca=random.choice(list(MARCAS_MODELOS.keys())),
        modelo=random.choice(random.choice(list(MARCAS_MODELOS.values()))),
        preco=random.randint(20000, 400000),
        tipo=random.choice(TIPOS),
        combustivel=random.choice(COMBUSTIVEIS),
        cor=random.choice(CORES),
        ano=random.randint(2004, 2024),
        km=random.randint(10000, 120000),
        portas = random.choice([2, 4]),
        transmissao = random.choice(["manual", "automática"]),
    )
    session.add(v)

session.commit()
session.close()
