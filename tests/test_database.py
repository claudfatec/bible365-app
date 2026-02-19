import pytest
from core.engine import carregar_progresso, salvar_progresso

def test_supabase_connection_and_persistence():
    # 1. Guarda o dia original para não estragar o teu progresso real
    dia_original = carregar_progresso()
    
    # 2. Tenta salvar um valor temporário (ex: dia 999)
    test_day = 66
    try:
        salvar_progresso(test_day)
        
        # 3. Verifica se o banco realmente guardou esse valor
        confirmacao = carregar_progresso()
        assert confirmacao == test_day
        
    finally:
        # 4. Limpeza: Volta sempre para o dia original, mesmo que o teste falhe
        salvar_progresso(dia_original)
