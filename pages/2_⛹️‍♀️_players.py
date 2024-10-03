import streamlit as st

st.set_page_config(
    page_title="Jogadores",
    page_icon="⛹️‍♀️",
    layout="wide"
)

df_data = st.session_state.data

# selecionando clubes
clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Clubes", clubes)
# filtrando por jogadores
df_players = df_data[df_data['Club'] == club]
players = df_players['Name'].value_counts().index
player = st.sidebar.selectbox("Jogadores", players)

# layout estaticas
player_stats = df_data[df_data['Name'] == player].iloc[0]
# carregando imagem
st.image(player_stats['Photo'])
st.title(player_stats['Name'])

# text
# st.markdown(f'*Clube:*' + player_stats['Club'])
st.markdown(f"*Clube:* {player_stats['Club']}")
st.markdown(f"*Posição:* {player_stats['Position']}")
# criando colunas
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"*Idade:* {player_stats['Age']}")
col2.markdown(f"*Altura:* {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"*Idade:* {player_stats['Weight(lbs.)']*0.453:.2f}")
st.divider()
# geral
st.subheader(f"Geral {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

# estatisticas 2
col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}")
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}")
col3.metric(label="Clausula de recição", value=f"£ {player_stats['Release Clause(£)']:,}")