#!/usr/bin/env -S python -m streamlit run
# 2024: ST Version 1.02

import streamlit as st
from transformers import pipeline
from acceptlang import parse_accept_lang_header


MODEL = 'Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime'
MODEL_URL = 'https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime'
MAX_LENGTH = 200


# The order of sentiments list matters!
MESSAGES = {
    'en': {
        'title': 'Sentiment Analysis (Transformers)',
        'usage': f'Estimate the sentiment expressed in the sentence. The eight classes of sentiments (emotions) are: *joy, sadness, anticipation, surprise, anger, fear, disdust, and trust*. The most prevalent sentiment is selected. The Transformers model used is [`{MODEL}`](`{MODEL_URL}`).',
        'sentiments': 'joy, sadness, anticipation, surprise, anger, fear, disdust, trust'.split(', '),
        'prompt': 'Enter a Japanese sentence'
    },
    'ja': {
        'title': 'AI 感情分析（Transformers 使用）',
        'usage': f'入力した日本語文に書かれた感情を判定します。感情の種類は*喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪、信頼*の8種類で、文中で最も支配的なものが表示されます。使用しているモデルは[`{MODEL}`]({MODEL_URL})です。',
        'sentiments': '喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪、信頼'.split('、'),
        'prompt': '日本語の文を入力してください'
    }
    
}


def get_model(model=MODEL):
    try:
        pipe = pipeline('sentiment-analysis', model=model)
    except Exception as e:
        st.markdown(e)
    return pipe


def find_language():
    lang_default = 'en'
    lang_list = list(MESSAGES.keys())
    try:
        al_value = st.context.headers['accept-language']
        al_parsed = parse_accept_lang_header(al_value)
        for lang in al_parsed:
            if lang.name in lang_list:
                return lang.name

        return lang_default
    except:
        return lang_default


pipe = get_model()
messages = MESSAGES[find_language()]


st.title(messages['title'])
st.markdown(messages['usage'])

sentence = st.chat_input(messages['prompt'], max_chars=MAX_LENGTH)
if sentence is not None:
    result = pipe(sentence)
    label_number = int(result[0]['label'][-1:])
    sentiment = messages['sentiments'][label_number]
    st.markdown(f'{sentence} >> **{sentiment}**')
