# Agente virtual + MCP + LLM

- Projeto desenvolvido para aplicar o conceito de agente virtual utilizando arquitetura independente entre o agente(cliente mcp), servidor MCP, e banco de dados

- Conteiners separados dividindo a aplicação python e o servidor LLM

## Executar projeto

- Criar e subir conteiners
```docker compose up -d```

- Baixar llm mistral
```./pull_mistral.sh```

- Popular o banco de dados
```./seed_database.sh```

- Executar agente
```./exec_agente.sh```

- Executar teste automatizado
```./run_tests.sh```
