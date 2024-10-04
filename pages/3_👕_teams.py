import streamlit as st

st.set_page_config(
    page_title="Times",
    page_icon="👕",
    layout="wide")
df_data = st.session_state.data

clubes = df_data['Club'].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtrado = df_data[(df_data['Club'] == club)].set_index('Name')

# pegar imagem do clube
st.image(df_filtrado.iloc[0]['Club Logo'])
st.markdown(f"##{club}")

# mostrar colunas
columns = ['Age', 'Photo', 'Flag', 'Overall',
           'Value(£)', 'Wage(£)', 'Joined', 'Height(cm.)',
       'Weight(lbs.)','Contract Valid Until', 'Release Clause(£)']
# config colunas
st.dataframe(df_filtrado[columns],
            column_config={
                'Overall': st.column_config.ProgressColumn(
                    'Overall', format="%d", min_value=0, max_value=100
                ),
                'Wage(£)': st.column_config.ProgressColumn(
                    'Weekly Wage', format="£%f", min_value=0, max_value=df_filtrado['Wage(£)'].max()
                ),
                "Photo": st.column_config.ImageColumn(),
                "Flag": st.column_config.ImageColumn("Country"),
            })