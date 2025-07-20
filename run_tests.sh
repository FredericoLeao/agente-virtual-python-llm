#!/bin/bash
docker compose exec -it app-python python -m pytest tests/test_agente.py
