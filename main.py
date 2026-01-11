import json

def carregar_dados():
    with open('data/biblia.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def calcular_plano_detalhado():
    livros = carregar_dados()
    total_capitulos = sum(l['capitulos'] for l in livros)
    media_diaria = total_capitulos / 365
    
    print(f"Total de capítulos carregados: {total_capitulos}")
    print(f"Meta diária aproximada: {media_diaria:.2f} capítulos")
    
    # Aqui entrará a lógica para distribuir os nomes dos livros
    # que faremos na próxima Sprint.

if __name__ == "__main__":
    calcular_plano_detalhado()