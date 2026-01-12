import json
import math

def gerar_cronograma_completo(): # <--- Nome padronizado aqui
    with open('data/biblia.json', 'r', encoding='utf-8') as f:
        livros = json.load(f)

    todos_capitulos = []
    for livro in livros:
        for cap in range(1, livro['capitulos'] + 1):
            todos_capitulos.append(f"{livro['livro']} {cap}")

    total_caps = len(todos_capitulos)
    cronograma = {}

    for dia in range(1, 366):
        inicio = math.floor((dia - 1) * (total_caps / 365))
        fim = math.floor(dia * (total_caps / 365))
        
        # Garante que o dia sempre tenha conteúdo se houver capítulos
        if inicio == fim and inicio < total_caps:
            fim = inicio + 1
            
        cronograma[dia] = todos_capitulos[inicio:fim]

    return cronograma