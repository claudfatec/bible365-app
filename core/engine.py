import json
import math

def gerar_cronograma_resumido():
    with open('data/biblia.json', 'r', encoding='utf-8') as f:
        livros = json.load(f)

    # Criamos a lista linear de capítulos
    todos_capitulos = []
    for livro in livros:
        for cap in range(1, livro['capitulos'] + 1):
            todos_capitulos.append(f"{livro['livro']} {cap}")

    total_caps = len(todos_capitulos)
    dias_plano = 365
    cronograma = {}

    for dia in range(1, dias_plano + 1):
        inicio_idx = math.floor((dia - 1) * (total_caps / dias_plano))
        fim_idx = math.floor(dia * (total_caps / dias_plano))
        
        # Ajuste para garantir que sempre haja progresso se houver capítulos disponíveis
        if inicio_idx == fim_idx and inicio_idx < total_caps:
            fim_idx = inicio_idx + 1
        
        caps_do_dia = todos_capitulos[inicio_idx:fim_idx]
        
        if caps_do_dia:
            primeiro = caps_do_dia[0]
            ultimo = caps_do_dia[-1]
            if primeiro == ultimo:
                cronograma[dia] = primeiro
            else:
                cronograma[dia] = f"{primeiro} a {ultimo}"
        else:
            cronograma[dia] = "Leitura concluída ou sem capítulos para este período"

    return cronograma

if __name__ == "__main__":
    plano = gerar_cronograma_resumido()
    print(f"Dia 1: {plano[1]}")
    print(f"Dia 2: {plano[2]}")