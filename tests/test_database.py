import pytest
import streamlit as st
from core.engine import carregar_progresso, salvar_progresso

def test_supabase_connection_and_persistence():
    # 1. Valor de teste único
    test_day = 66 
    
    # Salva o original para restaurar depois
    dia_original = carregar_progresso()
    
    try:
        # 2. Tenta salvar
        salvar_progresso(test_day)
        
        # 3. Limpa o cache do Streamlit para este teste específico
        # Isso garante que a próxima leitura vá ao banco de fato
        st.cache_data.clear()
        st.cache_resource.clear()
        
        # 4. Lê novamente
        confirmacao = carregar_progresso()
        
        assert confirmacao == test_day
        
    finally:
        # Restaura o dia real do usuário
        salvar_progresso(dia_original)