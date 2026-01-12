import streamlit as st
from core.engine import gerar_cronograma_resumido

# Configuração da página
st.set_page_config(page_title="Bible365 MVP", page_icon="📖")

st.title("📖 Meu Plano de Leitura 365 Dias")
st.subheader("Protótipo de Teste")

# Carrega o cronograma
with st.spinner('Gerando seu plano anual...'):
    plano = gerar_cronograma_resumido()

# Interface de usuário
dia_selecionado = st.number_input("Digite o dia da jornada (1-365):", min_value=1, max_value=365, value=1)

st.info(f"📅 **Para o Dia {dia_selecionado}, sua leitura é:**")
st.header(plano[dia_selecionado])

# Simulação de Checkbox de progresso
if st.checkbox("Marcar leitura de hoje como concluída"):
    st.success("Parabéns! Progresso salvo (simulação).")
    st.balloons()