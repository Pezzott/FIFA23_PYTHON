import streamlit as st
import pandas as pd 
import webbrowser
from datetime import datetime

st.set_page_config(
    page_title="Home",
    page_icon="⚽",  
    layout="wide"
)

# URL da imagem da FIFA
fifa_image_url = "https://media.contentapi.ea.com/content/dam/ea/fifa/fifa-23/world-cup/images/2022/10/f23-worldcup-featureimg-16x9.jpg.adapt.crop191x100.628p.jpg"

# Adicione a imagem da FIFA no topo da barra lateral
st.sidebar.image(fifa_image_url, use_column_width=True)

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.write("# FIFA 2023! ⚽")

st.sidebar.markdown("Desenvolvido por Adenilton Pezzott")

btn = st.button("Acesse este dados no kaggle")
if btn:
    webbrowser.open_new("https://www.kaggle.com/datasets/kevwesophia/fifa23-official-datasetclean-data")

st.markdown("""
<style>
.justifytext {
    text-align: justify;
    text-justify: inter-word;
}
</style>

<div class="justifytext">

**Conjunto de Dados de Jogadores de Futebol 2023**

O Conjunto de Dados de Jogadores de Futebol de 2023 fornece informações abrangentes sobre jogadores de futebol profissionais. O conjunto de dados contém uma ampla gama de atributos, incluindo demografia dos jogadores, características físicas, estatísticas de jogo, detalhes de contrato e afiliações a clubes. **Com mais de 17.000 registros**, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol, pois permite estudar atributos dos jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento de jogadores ao longo do tempo.

O Conjunto de Dados de Jogadores de Futebol de 2023 é uma coleção abrangente de informações sobre jogadores de futebol profissionais. Inclui detalhes como demografia dos jogadores, características físicas, estatísticas de jogo, detalhes de contrato, afiliações a clubes, valores de mercado, salários, posições preferidas, taxas de trabalho, avaliações de habilidades e desenvolvimento de jogadores.

</div>
""", unsafe_allow_html=True)