#!/usr/bin/env python
# 書籍版 pp. 102-103 から青空文庫 Zip をばらすコードを抜いたもの（UTF-8 プレーンテキストファイルを想定する）
# Transformers v4.51.3 で動作確認。

import re
import sys
import transformers
from transformers import pipeline

MODEL = 'Mizuiro-sakura/luke-japanese-large-sentiment-analysis-wrime'
SENTIMENTS = '喜び、悲しみ、期待、驚き、怒り、恐れ、嫌悪、信頼'.split('、')


def get_model(model=MODEL):
    pipe = pipeline("sentiment-analysis", model=model)
    return pipe


def get_sentiment(pipe, sentence):
    results = pipe(sentence)
    label_number = int(results[0]['label'][-1:])
    return SENTIMENTS[label_number]


def read_file(filename):
    with open(filename, 'r') as fp:
        body = fp.read()

    paragraphs = [par for par in re.split(r'[\r\n]+', body) if len(par) > 0]
    sentences = []
    for par in paragraphs:
        sentences.extend([s.strip() for s in re.split(r'。[」』]*', par) if len(s) > 0])

    return sentences



if __name__ == '__main__':
    print(f'Transformers version {transformers.__version__}')
    filename = sys.argv[1]
    sentences = read_file(filename)
    print(f'Read file: {filename}. 文の数: {len(sentences)}.')

    pipe = get_model();
    emotions = [get_sentiment(pipe, sentence) for sentence in sentences]
    stats = {e: emotions.count(e) for e in SENTIMENTS}
    print(stats)
