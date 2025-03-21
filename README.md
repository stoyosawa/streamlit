# Streamlit Sample Programs

<img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width="300">

このリポジトリでは、[Streamlit](https://streamlit.io/)＋[Python](https://docs.python.org/ja/3/)ベースのWebアプリケーション2点のコードを公開しています。カードゲームのブラックジャックと、[Hugging Face](https://huggingface.co/)にあるモデルを用いた感情分析アプリです。これらはStreamlitコミュニティで運用されているので、以下のURLから実際に試せます。

- Blackjack ... [https://sat-blackjack.streamlit.app/](https://sat-blackjack.streamlit.app/)
- Sentiment analysis ... [https://sat-sentiment.streamlit.app/](https://sat-sentiment.streamlit.app/)

Streamlitコミュニティ上のアプリケーションはしばらく使われていないと退蔵されます。そうした状態でアクセスがあると、まず「起こしますか？」（再度起動させる）というメッセージが出ます。クリックすれば展開が開始されますが、けっこう時間がかかります。とくに感情分析アプリは大きめなモデルやTransformersなどのパッケージがロードされる時間もあるので、かなり長く待たされます。ご了承のほどを。

これらアプリケーションは、『[作ってわかる［入門］Streamlit](https://gihyo.jp/book/2025/978-4-297-14764-8)』（技術評論社，2025年2月刊，400頁）の第9章と第3章でそれぞれ紹介したものです。書籍のものとコードがやや異なりますが、エッセンスは同じです。

The sentiment application uses a model trained on Japanese corpus. The program accepts any texts but you should not expect it outputs any meaningful result. 

【
<a href="https://gihyo.jp/book/2025/978-4-297-14764-8">技術評論社</a> |
<a href="https://www.amazon.co.jp/dp/4297147645">Amazon.co.jp</a> |
<a href="https://www.yodobashi.com/product/100000009004071953/">ヨドバシ</a> |
<a href="https://books.rakuten.co.jp/rk/bbc9cea531f231fc8be07aff0d7da559/">楽天</a>
】

<img src="http://image.gihyo.co.jp/assets/images/cover/2025/9784297147648.jpg" height="400">