import streamlit as st

st.set_page_config(
    page_title="Times",
    page_icon="⚽",  
    layout="wide"
)

# URL da imagem da FIFA
fifa_image_url = "https://media.contentapi.ea.com/content/dam/ea/fifa/fifa-23/world-cup/images/2022/10/f23-worldcup-featureimg-16x9.jpg.adapt.crop191x100.628p.jpg"

# Adicione a imagem da FIFA no topo da barra lateral
st.sidebar.image(fifa_image_url, use_column_width=True)

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clube", clubes)

df_filtered = df_data[df_data["Club"] == club].set_index("Name")

# Verifique se a coluna "Club Logo" existe no DataFrame antes de tentar exibir a imagem.
if "Club Logo" in df_filtered.columns:
    st.image(df_filtered.iloc[0]["Club Logo"], width=40)

st.markdown(f"## {club}")

# Lista de colunas a serem exibidas.
columns = ["Age", "Photo", "Flag", "Overall", "Value(£)", "Wage(£)",
           "Height(cm.)", "Weight(lbs.)", 'Contract Valid Until', 'Release Clause(£)',
           'Joined']

# Certifique-se de que a coluna 'Overall' exista no DataFrame.
if 'Overall' in df_filtered.columns:
    # Atualize a coluna 'Overall' com barras de progresso formatadas como HTML.
    df_filtered["Overall"] = df_filtered["Overall"].apply(lambda x: 
        f'<div style="width: 100%; height: 24px; background: #eee; border-radius: 12px; overflow: hidden;">'
        f'<div style="width: {x}%; height: 100%; background-color: #76b900; display: flex; align-items: center; justify-content: center; color: white;">'
        f'{x}</div></div>')

# Atualize a coluna 'Photo' para exibir as imagens dos jogadores.
if 'Photo' in df_filtered.columns:
    df_filtered['Photo'] = df_filtered['Photo'].apply(lambda url: f'<img src="{url}" width="60" height="60">')
    
# Atualize a coluna 'Flag' para exibir as imagens das bandeiras.
if 'Flag' in df_filtered.columns:
    df_filtered['Flag'] = df_filtered['Flag'].apply(lambda url: f'<img src="{url}" width="30" height="20">')

# Exiba o DataFrame com as colunas selecionadas usando HTML e permitindo HTML inseguro.
# Usamos 'st.markdown' para renderizar HTML e 'to_html(escape=False)' para gerar a string HTML do DataFrame.
html = df_filtered[columns].to_html(escape=False, index=False)
st.markdown(html, unsafe_allow_html=True)
