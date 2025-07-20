import json
import asyncio
from repository import buscar_veiculos

async def handle_client(reader, writer):
    data = await reader.readline()
    filtros = json.loads(data.decode())
    veiculos = buscar_veiculos(filtros)
    writer.write(json.dumps(veiculos).encode())
    await writer.drain()
    writer.close()

async def start_mcp_server():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 5555)
    print("Servidor MCP rodando em 127.0.0.1:5555")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(start_mcp_server())