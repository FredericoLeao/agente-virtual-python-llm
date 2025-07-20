from pydantic import BaseModel, ConfigDict


class VeiculoSchema(BaseModel):
    id: int
    marca: str | None = None
    modelo: str | None = None
    preco: float | None = None
    tipo: str | None = None
    combustivel: str | None = None
    cor: str | None = None
    ano: int | None = None
    km: int | None = None
    transmissao: str | None = None
    portas: int | None = None

    model_config = ConfigDict(from_attributes=True)
