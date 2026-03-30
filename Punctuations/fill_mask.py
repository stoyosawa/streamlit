#!/usr/bin/env python

from janome.tokenizer import Tokenizer
from transformers import pipeline

TASK = 'fill-mask'
MODEL = 'tohoku-nlp/bert-base-japanese'

def splitter(text):
    t = Tokenizer()
    text = ''.join(text.split())
    tokens = [w.surface for w in t.tokenize(text)]
    masked_text = '[MASK]'.join(tokens) + '[MASK]'

    pipe = pipeline(TASK, model=MODEL)
    results = pipe(masked_text)

    replaced = []
    for res, token in zip(results, tokens):
        first = res[0]
        replaced.append(token)
        if first['token_str'] in ['、', '。'] and first['score'] > 0.3:
            replaced.append(first['token_str'])

    return ''.join(replaced)



if __name__ == '__main__':
    from sys import argv
    text = ''.join(argv[1:])
    sentences = splitter(text)
    print(sentences)
