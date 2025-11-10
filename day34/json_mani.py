import json
from typing import Any

def salvar_dados(arquivo: str, dados: Any) -> None:
    
    with open(arquivo, 'w', encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)


def carregar_dados(arquivo:str) -> Any:

    try:
        with open(arquivo, 'r', encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("O arquivo não foi encontrado, caminho do arquivo {arquivo}")
        return {}
    
dados_exemplos = {"nome": "Robson", "cidade":"MG", "cargo":"Analista"}

nome_arquivo = "nome_lucas.json"

salvar_dados(nome_arquivo, dados_exemplos)

dados_carregados = carregar_dados(nome_arquivo)

print("Dados carregados:", dados_carregados)