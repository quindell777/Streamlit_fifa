import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    st.session_state["data"] = df_data

st.markdown("# JOGADORES FUTEBOL 2023! ⚽")
st.sidebar.markdown('Desenvolvido por [Riquelme Jorge](https://www.youtube.com/shorts/X9FNzyFDhSw)')

botao = st.button('Acompanhe os dados na fonte')

if botao:
    webbrowser.open_new_tab('https://www.fifaindex.com/pt-br/players/fifa23/')
st.markdown(
    """
    O JOGADORES FUTEBOL 2024! É uma aplicação de teste desenvolvida por mim, afim de testar meus avanços com o Streamlit
    Não tem o que ler aqui, é pura encheção de linguíça para testar o markdown, então pule todo o restante do texto e vá para as abas laterais.
    O futebol, um esporte jogado com os pés, tem visto muitos avanços nas últimas décadas. Os times
    estão melhores, com jogadores mais preparados. A tecnologia também ajudou, com coisas como
    VAR e gramados melhores. Clubes investem mais em jogadores caros e na estrutura, o que atrai
    mais torcedores. As regras mudaram um pouco, deixando o jogo mais rápido e com menos
    interrupções. Grandes estrelas, como Messi e Ronaldo, marcaram a era atual, trazendo muitos títulos
    para seus clubes. Os torcedores, por sua vez, continuam apaixonados pelo esporte.
    
    Cara, não perde teu tempo lendo aqui.

    Ok, Aí vai!
    Vini Jr. é simplesmente brilhante, uma verdadeira joia do futebol mundial. Sua velocidade, habilidade
    e criatividade em campo são nada menos que espetaculares. Cada vez que ele toca na bola, é como
    se o jogo ganhasse uma nova dimensão, com dribles desconcertantes e jogadas imprevisíveis que
    deixam defensores e espectadores sem fôlego. A maneira como ele enfrenta adversários com
    coragem e confiança é inspiradora, sempre buscando o gol e criando oportunidades para seu time.
    Além de seu talento natural, Vini Jr. é extremamente dedicado e trabalha incansavelmente para
    melhorar cada aspecto do seu jogo. Sua ascensão meteórica no Real Madrid é um testemunho de
    sua ética de trabalho e de sua paixão pelo futebol. Ele é, sem dúvida, um dos jogadores mais
    emocionantes da nova geração, e seu futuro promete ser ainda mais brilhante, já consolidado como
    uma estrela de nível mundial.

    ***VINI JUNIOR BOLA DE OURO 2024!***
    """
)