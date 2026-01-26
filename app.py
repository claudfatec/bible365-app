import streamlit as st
from core.engine import carregar_jornada, carregar_progresso, salvar_progresso

st.set_page_config(page_title="Bible365 Journey", page_icon="📖")

# Título e Progresso
st.title("📖 Minha Jornada Bíblica")

jornada = carregar_jornada()
dia_atual = carregar_progresso()
total_dias = len(jornada)

# Barra de Progresso Visual
progresso_percent = (dia_atual - 1) / total_dias
st.progress(progresso_percent)
st.write(f"Você completou **{int(progresso_percent*100)}%** da jornada (Dia {dia_atual} de {total_dias})")

st.divider()

# Conteúdo do Dia
if dia_atual <= total_dias:
    texto_dia = jornada[dia_atual - 1]
    # Transforma a string de trechos em uma lista para o checklist
    trechos = [t.strip() for t in texto_dia.split(',')]
    
    st.subheader(f"Leituras para o Dia {dia_atual}:")
    
    # Gerar checklists individuais
    concluidos = []
    for trecho in trechos:
        check = st.checkbox(f"Ler {trecho}", key=f"dia{dia_atual}_{trecho}")
        concluidos.append(check)
    
    st.divider()
    
    # Botão para avançar de dia
    if all(concluidos):
        if st.button("Finalizar Dia e Avançar ➔"):
            salvar_progresso(dia_atual + 1)
            st.balloons()
            st.rerun()
    else:
        st.info("Marque todos os trechos acima para concluir o dia.")
else:
    st.success("🎉 Parabéns! Você completou todo o plano de leitura!")
    if st.button("Reiniciar Jornada"):
        salvar_progresso(1)
        st.rerun()