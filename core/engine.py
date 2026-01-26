import json
import os

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