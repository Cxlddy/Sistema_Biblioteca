import json
import os

CAMINHO_DB = os.path.join(os.path.dirname(__file__), "database.json")


def carregar_dados():
    try:
        with open(CAMINHO_DB, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {"livros": [], "usuarios": []}


def salvar_dados(dados):
    with open(CAMINHO_DB, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)