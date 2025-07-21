import json
import requests
import asyncio

MCP_SERVER = "127.0.0.1"
LLM_OLLAMA_SERVER = "llm-ollama"

def formatar_output_agente(res: list):
    output = f"\n{len(res)} carros encontrados!"
    for veiculo in res:
        v = veiculo
        output += (
            f"\n- {v['marca']} {v['modelo']} {v['ano']} ({v['tipo']} | "
            f"{v['cor']}, {v['km']} km, {v['transmissao']} "
            f"({v['portas']} portas) | {v['combustivel']} | "
            f"R${v['preco']:.2f}")
    return output

async def consultar_servidor_mcp(filtros: str):
    reader, writer = await asyncio.open_connection(MCP_SERVER, 5555)
    writer.write((str(filtros) + "\n").encode())
    await writer.drain()

    data = await reader.readline()
    res = data.decode()

    writer.close()
    await writer.wait_closed()

    return res

def consultar_llm_local(prompt: str, model: str = "mistral") -> str:
    response = requests.post(
        f"http://{LLM_OLLAMA_SERVER}:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"].strip()

def extrair_filtros(input_usuario: str) -> dict:
    prompt = f"""
Sua função é extrair filtros de busca de carros a partir de frases em linguagem natural.

Responda com um JSON válido contendo apenas os filtros mencionados

Campos válidos (todos opcionais):
- marca: lista de strings
- modelo: string
- ano_min: inteiro
- preco_max: inteiro (em reais)
- combustivel: string (ex: gasolina, etanol, flex, diesel)
- tipo: string (ex: SUV, sedan, hatch, pickup)
- cor: string
- km_max: inteiro
- transmissao: string
- portas: inteiro

Retorne **apenas** o JSON

Exemplo de entrada:
"Quero um SUV da Jeep, azul, diesel, de 2020 pra cima, até 100 mil reais, com até 60 mil km, transmissao automatica"

Exemplo de saída:
{{
  "tipo": "SUV",
  "marca": ["Jeep"],
  "combustivel": "diesel",
  "ano_min": 2020,
  "preco_max": 100000,
  "km_max": 60000,
  "cor": "azul",
  "transmissao": "automatica"
}}

Agora processe esta frase:
"{input_usuario}"
"""
    return json.dumps(
        json.loads(consultar_llm_local(prompt)),
        separators=(',', ':'))

async def executar_agente():
    print("\nOlá, posso te ajudar na sua busca por um carro")
    u_input = ''
    while u_input.lower() != 'sair':
        print("\nMe diga que tipo de carro deseja procurar\n")
        u_input = input("\n> ")
        print("\nOk, procurando...\n")
        filtros = extrair_filtros(u_input)
        # consultar servidor mcp
        res = json.loads(await consultar_servidor_mcp(filtros))
        # receber resultado e exibir para o usuário
        if not res or len(res) == 0:
            print("\nNenhum carro encontrado, tente novamente")
            continue

        print(formatar_output_agente(res))

if __name__ == "__main__":
    asyncio.run(executar_agente())
