## Adding punctuations

This streamlit program insets punctuations to the appropriate positions in a given Japanese text.

The code breaks down the text into tokens and inserts `[MASK]` between the tokens. A fill-mask task then finds the appropriate characters to the `[MASK]`. The `[MASK]` is replaced when the characters are (`、` or `。`) and the score (probability) is larger than 0.3.

Hugging Face `transformers.pipe` is used. The model employed is [`tohoku-nlp/bert-base-japanese`](https://huggingface.co/tohoku-nlp/bert-base-japanese).

The code appears in Section 7.6 of the book "Hands on Streamlit" (Gihyo 2025).
