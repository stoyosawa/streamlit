#!/usr/bin/env -S python -m streamlit run
# 2024: ST Version 1.02

import streamlit as st
from transformers import pipeline


MODEL = 'Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime'
MODEL_URL = 'https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime'
MAX_LENGTH = 200

messages = {
    'title': 'AI 感情分析（Transformers 使用）',
    'usage': f'入力した日本語文に書かれた感情を判定します。感情の種類は*喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪、信頼*の8種類で、文中で最も支配的なものが表示されます。使用しているモデルは[`{MODEL}`]({MODEL_URL})です。',
    'sentiments': '喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪、信頼'.split('、'),
    'prompt': '日本語の文を入力してください'
}


@st.cache_resource
def get_model(model=MODEL):
    try:
        pipe = pipeline('sentiment-analysis', model=model)
    except Exception as e:
        st.markdown(e)
    return pipe


with st.sidebar:
    st.markdown('本アプリケーションは、[『作ってわかる［入門］Streamlit』](https://gihyo.jp/book/2025/978-4-297-14764-8)の第3章で紹介したものです。コードの説明やクラウドへの展開方法などはそちらを参照してください。')
    st.image('http://image.gihyo.co.jp/assets/images/cover/2025/9784297147648.jpg')


pipe = get_model()
st.title(messages['title'])
st.markdown(messages['usage'])

sentence = st.chat_input(messages['prompt'], max_chars=MAX_LENGTH)
if sentence is not None:
    result = pipe(sentence)
    label_number = int(result[0]['label'][-1:])
    sentiment = messages['sentiments'][label_number]
    st.markdown(f'{sentence} >> **{sentiment}**')
