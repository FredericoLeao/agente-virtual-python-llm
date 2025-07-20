from agente import formatar_output_agente

def test_resposta_agente():
    res_db_mock = [
        {
            "marca": "Fiat",
            "modelo": "Uno",
            "ano": 2019,
            "cor": "prata",
            "km": 45000,
            "transmissao": "manual",
            "portas": 4,
            "tipo": "sedan",
            "combustivel": "flex",
            "preco": 35200.0
        },
        {
            "marca": "Chevrolet",
            "modelo": "Onix",
            "ano": 2020,
            "cor": "prata",
            "km": 45000,
            "transmissao": "automatico",
            "tipo": "hatch",
            "portas": 4,
            "combustivel": "flex",
            "preco": 58200.0
        }
    ]
    output = formatar_output_agente(res_db_mock)
    assert "Chevrolet Onix 2020" in output
    assert "Fiat Uno 2019" in output
