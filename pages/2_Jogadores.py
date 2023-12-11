import streamlit as st

st.set_page_config(
    page_title="Jogadores",
    page_icon="⚽",  
    layout="wide"
)

# URL da imagem da FIFA
fifa_image_url = "https://media.contentapi.ea.com/content/dam/ea/fifa/fifa-23/world-cup/images/2022/10/f23-worldcup-featureimg-16x9.jpg.adapt.crop191x100.628p.jpg"

# Adicione a imagem da FIFA no topo da barra lateral
st.sidebar.image(fifa_image_url, use_column_width=True)

# Supondo que "data" já esteja carregada em st.session_state["data"]
df_data = st.session_state["data"]

# Seleção de clube
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

# Filtragem de jogadores por clube
df_players = df_data[df_data["Club"] == club]
players = df_players["Name"].unique()  # Usar unique() para obter uma lista de nomes únicos
player = st.sidebar.selectbox("Jogador", players)

# Filtragem de estatísticas por jogador selecionado
player_stats = df_players[df_players["Name"] == player].iloc[0]  # Usar colchetes para indexação

# Exibição da foto do jogador
st.image(player_stats["Photo"])
st.title(f"{player_stats['Name']}")

st.markdown(f" **Clubes:** {player_stats['Club']}")
st.markdown(f" **Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)

col1.markdown((f" **Idade:** {player_stats['Age']}"))
col2.markdown((f" **Altura:** {player_stats['Height(cm.)'] / 100}"))
col3.markdown((f" **Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}"))

st.divider()
st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3 = st.columns(3)

col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']:,}" )
col2.metric(label="Remuneração semanal", value=f"£ {player_stats['Wage(£)']:,}" )
col3.metric(label="Cláusula de rescisão", value=f"£ {player_stats['Release Clause(£)']:,}" )