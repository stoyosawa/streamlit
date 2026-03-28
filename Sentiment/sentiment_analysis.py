#!/usr/bin/env -S python -m streamlit run
# 2024: ST Version 1.02
# 2026: ST Version 1.10 ... 日英対応。注意：Transformers は version 4.51.3 を使用のこと。

import streamlit as st
import transformers
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

MODEL_NAME = 'Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime'
MODEL_URL = 'https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime'
BOOK_URL = 'https://gihyo.jp/book/2025/978-4-297-14764-8'
BOOK_IMG = 'http://image.gihyo.co.jp/assets/images/cover/2025/9784297147648.jpg'

MAX_LENGTH = 200

MESSAGES = {
    'jp': {
        'title': 'AI 感情分析（Transformers 使用）',
        'usage': f'入力した日本語文に書かれた感情を判定します。感情の種類は*喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪、信頼*の8種類で、文中で最も支配的なものが表示されます。使用しているモデルは[`{MODEL_NAME}`]({MODEL_URL})です。Transformers には v4 を使います（v4.51.3で動作確認しました）。',
        'sentiments': '喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪、信頼'.split('、'),
        'prompt': '日本語の文を入力してください',
        'description': f'本アプリケーションは、[『作ってわかる［入門］Streamlit』]({BOOK_URL})の第3章で紹介したものです。コードの説明やクラウドへの展開方法などはそちらを参照してください。'
    },
    'en': {
        'title': 'AI-Powered Sentiment Analysis (with Transformers)',
        'usage': f'This app determines the emotion expressed in the Japanese text you enter. It classifies emotions into eight categories — joy, sadness, anticipation, surprise, anger, fear, disgust, and trust — and displays the one that is most dominant in the sentence. The model used for the analysis is [`{MODEL_NAME}`]({MODEL_URL}). Use transformers v4 (tested on v4.51.3).',
        'sentiments': 'joy, sadness, anticipation, surprise, anger, fear, disgust, trust'.split(', '),
        'prompt': 'Enter a Japanese text',
        'description': f'This app is introduced in Chapter 3 of [“Hands-on Streamlit”]({BOOK_URL}).'
    }
}

@st.cache_resource
def get_model(model_name=MODEL_NAME):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    pipe = pipeline("sentiment-analysis",
        model=model,
        tokenizer=tokenizer
    )

    return pipe


lang = 'jp'         # default
with st.sidebar:
    lang = st.radio('dummy',
        options=MESSAGES.keys(),
        index=0,
        horizontal=True,
        label_visibility="hidden"
    )
    st.markdown(MESSAGES[lang]['description'])
    st.image(BOOK_IMG)

    st.markdown(f'Transformers version {transformers.__version__}')


pipe = get_model()
st.title(MESSAGES[lang]['title'])
st.markdown(MESSAGES[lang]['usage'])

sentence = st.chat_input(MESSAGES[lang]['prompt'], max_chars=MAX_LENGTH)
if sentence is not None:
    result = pipe(sentence)
    label_number = int(result[0]['label'][-1:])
    sentiment = MESSAGES[lang]['sentiments'][label_number]
    st.markdown(f'{sentence} >> **{sentiment}**')
