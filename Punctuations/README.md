## Adding punctuations

This streamlit program insets punctuations to the appropriate positions in a given Japanese text.

The code breaks down the text into tokens and inserts `[MASK]` between the tokens. A fill-mask task then finds the appropriate characters to the `[MASK]`. The `[MASK]` is replaced when the characters are (`、` or `。`) and the score (probability) is larger than 0.3.

Hugging Face `transformers.pipe` is used. The model employed is [`tohoku-nlp/bert-base-japanese`](https://huggingface.co/tohoku-nlp/bert-base-japanese).

Use Python 3.13 or earlier. The [`SydachiPy`](https://pypi.org/project/SudachiPy/#files) wheel for Python 3.14 is not yet available. The author tested on 3.12.3.

Streamlir Community Cloud uses Python 3.14 by default. Change the version to 3.12 from the app settings:

<img src="python_version.png" width="800">

The code appears in Section 7.6 of the book "Hands on Streamlit" (Gihyo 2025).
