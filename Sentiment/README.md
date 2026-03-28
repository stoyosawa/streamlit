# Sentiment analysis

😄 😢 🙂 😲 😠 😨 🤢 🤢

This app determines the emotion expressed in the Japanese sentence you enter. It classifies emotions into eight categories — joy (喜び), sadness (悲しみ), anticipation (期待), surprise (驚き), anger (怒り), fear (恐れ), disgust (嫌悪), and trust (信頼) — and displays the one that is most dominant in the sentence.

The model used for the analysis is from Hugging Face: [Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime](https://huggingface.co/Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime). `Transofrmers` is used. The code is prepared for an entry‑level Python/Streamlt programming class.

To play, visit the Streamlit Community Cloud: [https://sat-sentiment.streamlit.app/](https://sat-sentiment.streamlit.app/)

Tested on transformers version 4.51.3. Does not work with v5 or later.
