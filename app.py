import streamlit as st
from core.engine import carregar_jornada, carregar_progresso, salvar_progresso, expandir_trecho

st.set_page_config(page_title="Bible365 Journey", page_icon="📖")

# --- Lógica de Reset na Barra Lateral ---
with st.sidebar:
    st.header("Configurações")
    if st.button("🔄 Reiniciar Jornada"):
        # Criamos um estado de confirmação para evitar resets acidentais
        st.session_state.confirm_reset = True

    if st.session_state.get('confirm_reset'):
        st.warning("Tem a certeza? Todo o progresso será perdido.")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Sim, Reset"):
                salvar_progresso(1)
                st.session_state.confirm_reset = False
                st.rerun()
        with col2:
            if st.button("Cancelar"):
                st.session_state.confirm_reset = False
                st.rerun()

# --- Conteúdo Principal (Mantendo a lógica anterior) ---
jornada = carregar_jornada()
dia_atual = carregar_progresso()

st.title(f"📖 Minha Jornada: Dia {dia_atual}")

if dia_atual <= len(jornada):
    texto_dia = jornada[dia_atual - 1]
    # Expande trechos (ex: 'Gn 1-3' vira ['Gn 1', 'Gn 2', 'Gn 3'])
    todos_capitulos = expandir_trecho(texto_dia)
    
    # Barra de progresso geral
    st.progress((dia_atual - 1) / len(jornada))
    
    st.subheader("Checklist de hoje:")
    concluidos = []
    for cap in todos_capitulos:
        check = st.checkbox(f"Ler {cap}", key=f"d{dia_atual}_{cap}")
        concluidos.append(check)
    
    st.divider()
    
    if all(concluidos):
        if st.button("Concluir Dia e Avançar ➔"):
            salvar_progresso(dia_atual + 1)
            st.balloons()
            st.rerun()
    else:
        st.info(f"Faltam {concluidos.count(False)} capítulos para concluir o dia.")
else:
    st.success("🎉 Parabéns! Completou todo o plano!")