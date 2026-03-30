import streamlit as st
import fill_mask

MESSAGES = {
    'ja': {
        'title': '句読点の挿入（和文）',
        'help': '句読点（、や。）のない読みにくい文章に句読点を挿入します。本プログラムは、『**作ってわかる［入門］Streamlit**』（技術評論社; 2025）の7.6節で説明したものを Streamlit 化したものです。Hugging Face `transformers` を使っています。モデルは `tohoku-nlp/bert-base-japanese` です。',
        'input_prompt': '日本語テキストを入力してください。'
    },
    'en': {
        'title': 'Inserting punctuations into Japanese text',
        'help': 'Powered by Hugging Face `transformers` with the `tohoku-nlp/bert-base-japanese` model. ',
        'input_prompt': 'Enter a Japanese text.'
    }
}


lang = 'ja'             # default
with st.sidebar:
    lang = st.radio('Dummy title',
        options=MESSAGES.keys(),
        label_visibility='hidden',
        index=0             # default japanese
    )

messages = MESSAGES[lang]

st.title('句読点の挿入', help=messages['help'])
text = st.text_area(messages['input_prompt'], value=None)
if text:
    sentences = fill_mask.splitter(text) 
    st.write(sentences)
