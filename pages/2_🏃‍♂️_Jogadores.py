import streamlit as st
import time

df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
clube = st.sidebar.selectbox("Clube", clubes)

jogadores = df_data[df_data["Club"] == clube]["Name"].unique()
jogador = st.sidebar.selectbox("Jogador", jogadores)

player_stats = df_data[df_data["Name"] == jogador].iloc[0]
st.image(player_stats["Photo"])
st.title(player_stats["Name"])
st.markdown(f"**Clube:** {player_stats['Club']}")
st.markdown(f"**Posição:** {player_stats['Position']}")

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)']*0.453: .2f}")
col4.markdown(f"**Valor de Mercado:** {player_stats['Value(£)']}")

st.subheader(f"Overall {player_stats['Overall']}")
st.progress(int(player_stats["Overall"]))

st.divider()

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de Mercado", value=f"£ {player_stats['Value(£)']}")
col2.metric(label="Remuneração", value=f"£ {player_stats['Wage(£)']}")
col3.metric(label="Cláusula de Rescisão", value=player_stats['Release Clause(£)'])