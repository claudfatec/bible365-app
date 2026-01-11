import json

def gerar_cronograma_completo():
    with open('data/biblia.json', 'r', encoding='utf-8') as f:
        livros = json.load(f)

    # Criamos uma lista linear de todos os capítulos: [("Gênesis", 1), ("Gênesis", 2)...]
    todos_capitulos = []
    for livro in livros:
        for cap in range(1, livro['capitulos'] + 1):
            todos_capitulos.append(f"{livro['livro']} {cap}")

    total_caps = len(todos_capitulos)
    caps_por_dia = total_caps / 365
    cronograma = {}

    for dia in range(1, 366):
        # Calculamos o índice de início e fim para este dia
        inicio = int((dia - 1) * caps_por_dia)
        fim = int(dia * caps_por_dia)
        
        # O último dia pega qualquer arredondamento restante
        if dia == 365:
            fim = total_caps
            
        cronograma[dia] = todos_capitulos[inicio:fim]

    return cronograma

# Testando o resultado
if __name__ == "__main__":
    plano = gerar_cronograma_completo()
    print(f"Dia 1: {', '.join(plano[1])}")
    print(f"Dia 2: {', '.join(plano[2])}")
