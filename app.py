import streamlit as st
from core.engine import carregar_jornada, carregar_progresso, salvar_progresso, expandir_trecho

st.set_page_config(page_title="Bible365", page_icon="📖", layout="centered")

# Inicialização do estado
if 'confirm_reset' not in st.session_state:
    st.session_state.confirm_reset = False
if 'jornada' not in st.session_state:
    st.session_state.jornada = carregar_jornada()
if 'dia_atual' not in st.session_state:
    st.session_state.dia_atual = carregar_progresso()

with st.sidebar:
    st.header("⚙️ Definições")
    
    total_dias = len(st.session_state.jornada)
    st.metric("Progresso", f"{st.session_state.dia_atual}/{total_dias}")
    
    if st.button("🔄 Reiniciar Jornada"):
        st.session_state.confirm_reset = True
    
    if st.session_state.confirm_reset:
        st.warning("Confirmar reset total?")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Sim"):
                salvar_progresso(1)
                st.session_state.dia_atual = 1
                st.session_state.confirm_reset = False
                st.rerun()
        with col2:
            if st.button("❌ Não"):
                st.session_state.confirm_reset = False
                st.rerun()

# Lógica Principal
jornada = st.session_state.jornada
dia_atual = st.session_state.dia_atual

st.title(f"📖 Dia {dia_atual}")

if dia_atual <= len(jornada):
    progresso_perc = (dia_atual - 1) / len(jornada)
    st.progress(progresso_perc, text=f"{int(progresso_perc * 100)}% completo")
    
    capitulos = expandir_trecho(jornada[dia_atual - 1])
    
    st.subheader("📋 Checklist de Leitura")
    checks = [st.checkbox(f"✓ {c}", key=f"d{dia_atual}_{c}") for c in capitulos]
    
    if all(checks) and len(checks) > 0:
        st.success("✅ Dia concluído!")
        if st.button("Próximo Dia ➔", use_container_width=True, type="primary"):
            salvar_progresso(dia_atual + 1)
            st.session_state.dia_atual = dia_atual + 1
            st.balloons()
            st.rerun()
else:
    st.balloons()
    st.success("🎉 Parabéns! Completou o plano anual!")
    if st.button("🔄 Recomeçar", use_container_width=True):
        salvar_progresso(1)
        st.session_state.dia_atual = 1
        st.rerun()