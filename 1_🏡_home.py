import streamlit as st
import pandas as pd 
from datetime import datetime

st.set_page_config(
    page_title="Home",
    page_icon="⚽",
    layout="wide"
)



if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data['Contract Valid Until'] >= datetime.today().year]
    df_data = df_data.sort_values(by='Overall', ascending=False) 
    st.session_state.data = df_data

st.markdown("# FIFA 23 OFFICIAL WEBSITE ⚽")
st.sidebar.markdown("Desenvolvido por: [Adson](https://github.com/Adson-C?tab=repositories)")

btn = st.link_button(
    "Acesso os dados do Fifa Kaggle", 
    "https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")
    
st.markdown(
    """    
    _summary_\n
    O Football Player Dataset de 2017 a 2023 fornece informações abrangentes sobre jogadores profissionais de futebol.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos do jogador, características físicas,
    estatísticas de jogo, detalhes do contrato e afiliações ao clube. Com mais de 17.000 registros, 
    este conjunto de dados oferece um recurso valioso para analistas, 
    pesquisadores e entusiastas do futebol interessados ​​em explorar vários aspectos do mundo do futebol, 
    pois permite estudar atributos do jogador, métricas de desempenho, avaliação de mercado, análise do clube,
    posicionamento do jogador e desenvolvimento do jogador ao longo do tempo.
    
    """
    )