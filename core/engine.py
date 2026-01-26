import json
import os
import re

CAMINHO_JORNADA = os.path.join('data', 'jornada.json')
CAMINHO_SAVE = os.path.join('data', 'save.txt')

def carregar_jornada():
    with open(CAMINHO_JORNADA, 'r', encoding='utf-8') as f:
        return json.load(f)

def carregar_progresso():
    if os.path.exists(CAMINHO_SAVE):
        with open(CAMINHO_SAVE, 'r') as f:
            return int(f.read())
    return 1 # Começa no dia 1 se não houver progresso salvo

def salvar_progresso(dia):
    with open(CAMINHO_SAVE, 'w') as f:
        f.write(str(dia))

def expandir_trecho(trecho):
    """
    Converte 'Gn 1-3' em ['Gn 1', 'Gn 2', 'Gn 3']
    """
    # Procura pelo padrão: Nome do Livro + Espaço + Inicio + Hífen + Fim
    match = re.search(r'(.+?)\s+(\d+)-(\d+)', trecho)
    
    if match:
        livro = match.group(1)
        inicio = int(match.group(2))
        fim = int(match.group(3))
        return [f"{livro} {cap}" for cap in range(inicio, fim + 1)]
    
    return [trecho] # Se não tiver hífen, retorna o próprio trecho em uma lista