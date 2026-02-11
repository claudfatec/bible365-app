import streamlit as st
from core.engine import carregar_jornada, carregar_progresso, salvar_progresso, expandir_trecho

# 1. Configuração e Inicialização de Estado
st.set_page_config(page_title="Bible365 Journey", page_icon="📖")

if 'confirm_reset' not in st.session_state:
    st.session_state.confirm_reset = False

# --- Lógica de Reset na Barra Lateral ---
with st.sidebar:
    st.header("⚙️ Configurações")
    if st.button("🔄 Reiniciar Jornada"):
        st.session_state.confirm_reset = True

    if st.session_state.confirm_reset:
        st.error("⚠️ Atenção!")
        st.write("Deseja apagar todo o progresso?")
        c1, c2 = st.columns(2)
        with c1:
            if st.button("✅ Sim"):
                salvar_progresso(1)
                st.session_state.confirm_reset = False
                st.rerun()
        with c2:
            if st.button("❌ Não"):
                st.session_state.confirm_reset = False
                st.rerun()

# --- Conteúdo Principal ---
try:
    jornada = carregar_jornada()
    dia_atual = carregar_progresso()
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.stop()

# Cabeçalho de Progresso
total_dias = len(jornada)
progresso_geral = min((dia_atual - 1) / total_dias, 1.0)

st.title(f"📖 Dia {dia_atual}")
st.progress(progresso_geral)
st.caption(f"Progresso total: {int(progresso_geral * 100)}% de {total_dias} dias")

if dia_atual <= total_dias:
    texto_dia = jornada[dia_atual - 1]
    todos_capitulos = expandir_trecho(texto_dia)
    
    st.subheader("📝 Checklist de Leitura")
    
    # Organizando os checkboxes
    concluidos = []
    for cap in todos_capitulos:
        # Chave única baseada no dia e no nome do capítulo
        is_checked = st.checkbox(f"Ler {cap}", key=f"d{dia_atual}_{cap}")
        concluidos.append(is_checked)
    
    st.divider()
    
    # Lógica de Finalização
    faltam = concluidos.count(False)
    
    if faltam == 0:
        st.success("🌟 Excelente! Todos os capítulos concluídos.")
        if st.button("Confirmar e Ir para o Próximo Dia ➔", use_container_width=True):
            salvar_progresso(dia_atual + 1)
            st.balloons()
            st.rerun()
    else:
        st.info(f"Faltam apenas **{faltam}** capítulos para concluir o dia de hoje. Vamos lá!")
else:
    st.balloons()
    st.success("🎉 **Incrível!** Você completou todo o plano de leitura!")
    st.write("Que tal começar uma nova jornada ou revisar seus livros favoritos?")