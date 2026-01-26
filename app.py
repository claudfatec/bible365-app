import streamlit as st
from core.engine import carregar_jornada, carregar_progresso, salvar_progresso, expandir_trecho

st.set_page_config(page_title="Bible365", page_icon="📖")

jornada = carregar_jornada()
dia_atual = carregar_progresso()

st.title(f"📖 Dia {dia_atual}")

if dia_atual <= len(jornada):
    texto_dia = jornada[dia_atual - 1]
    trechos_brutos = [t.strip() for t in texto_dia.split(',')]
    
    # Nova lógica: Expande os trechos antes de mostrar
    todos_capitulos = []
    for t in trechos_brutos:
        todos_capitulos.extend(expandir_trecho(t))
    
    st.write("Sua lista de leitura detalhada:")
    
    # Gerar checkboxes para cada capítulo expandido
    concluidos = []
    for cap in todos_capitulos:
        check = st.checkbox(f"Leia {cap}", key=f"d{dia_atual}_{cap}")
        concluidos.append(check)
    
    st.divider()
    
    if all(concluidos):
        if st.button("Concluir Dia e Avançar ➔"):
            salvar_progresso(dia_atual + 1)
            st.balloons()
            st.rerun()
    else:
        st.info(f"Faltam {concluidos.count(False)} capítulos para terminar hoje!")