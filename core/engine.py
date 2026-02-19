import streamlit as st
from st_supabase_connection import SupabaseConnection

def get_supabase_client():
    # Conecta usando os segredos configurados no Streamlit Cloud ou .streamlit/secrets.toml
    return st.connection("supabase", type=SupabaseConnection)

def carregar_jornada():
    # Mantemos o carregamento do JSON local pois ele é o nosso "dicionário" estático
    import json
    with open('data/jornada.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def carregar_progresso():
    try:
        supabase = get_supabase_client()
        # Busca o dia_atual para o ID 1 (uso pessoal)
        res = supabase.table("progresso").select("dia_atual").eq("id", 1).execute()
        if res.data:
            return res.data[0]['dia_atual']
        return 1
    except Exception:
        return 1

def salvar_progresso(novo_dia):
    try:
        supabase = get_supabase_client()
        # Atualiza o registo na nuvem
        supabase.table("progresso").update({"dia_atual": novo_dia}).eq("id", 1).execute()
    except Exception as e:
        st.error(f"Erro ao salvar progresso: {e}")

def expandir_trecho(trecho):
    if not trecho or '-' not in trecho:
        return [trecho] if trecho else [""]
    
    try:
        partes = trecho.split(' ')
        livro = " ".join(partes[:-1])
        caps = partes[-1].split('-')
        inicio, fim = int(caps[0]), int(caps[1])
        return [f"{livro} {i}" for i in range(inicio, fim + 1)]
    except:
        return [trecho]