import streamlit as st
from core.engine import gerar_cronograma_completo

st.set_page_config(page_title="Bible365", page_icon="📖")

st.title("📖 Bible365: Checklist")

# Gerar o plano
plano = gerar_cronograma_completo()

dia = st.number_input("Selecione o Dia", min_value=1, max_value=365, value=1)
capitulos_do_dia = plano.get(dia, [])

st.subheader(f"Leitura do Dia {dia}")

# Checklist
progresso = []
for cap in capitulos_do_dia:
    # O 'key' ajuda o Streamlit a manter o estado do checkbox
    check = st.checkbox(cap, key=f"chk_{dia}_{cap}")
    progresso.append(check)

# Validação de conclusão
if len(progresso) > 0 and all(progresso):
    st.success("Parabéns! Progresso salvo (simulação).")
    st.balloons()