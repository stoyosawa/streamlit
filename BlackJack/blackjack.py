#!/usr/bin/env -S python -m streamlit run

import streamlit as st
from random import shuffle

cards_surface = list('🂡🂢🂣🂤🂥🂦🂧🂨🂩🂪🂫🂭🂮'+'🂱🂲🂳🂴🂵🂶🂷🂸🂹🂺🂻🂽🂾'+'🃁🃂🃃🃄🃅🃆🃇🃈🃉🃊🃋🃍🃎'+'🃑🃒🃓🃔🃕🃖🃗🃘🃙🃚🃛🃝🃞')
cards_style = [f'<span style="font-size: 96px; color: {c};">' for c in ['MidnightBlue', 'Red', 'Red', 'MidnightBlue']]

st.set_page_config(page_title='Blackjack')
st.title('🂡 Blackjack 🂫')

with st.expander('How to play'):
    st.markdown('''
- You and the AI (artificial idiot) dealer are the only players.
- Press `Start` button to start. You are initially given two cards. To take another, press `Hit`. If your total exceeds 21, you automatically loose. Go to the next session.
- Once you are ready, press `Showdown`.
- The dealer deals cards for him. He is simple-minded. He takes cards until they reach 17. As long as the total is in between 17 and 21, he does not take any further. Naturally, when the total exceeds 21, he looses. 
- The JSON data on the sidebar shows the cummulative scores. To clear, reload from your browser button.
- This game only adds up numbers on the cards. Nothing fancy. It does not allow you to 'split' or 'double-down'. No bets either.
''')



def show_cards(cards_list, container):
    surfaces = []
    for c in cards_list:
        s = cards_surface[c]
        p = cards_style[int(c / 13)]
        surfaces.append(p + s + '</span>')

    container.html(' '.join(surfaces))


def calculate_score(cards_list):
    tmp = [num % 13 + 1 for num in cards_list]
    tmp = [10 if num >= 10 else num for num in tmp]
    tmp = [11 if num == 1 else num for num in tmp]

    # 21以上だったときは、11を1に直して再計算する
    while sum(tmp) > 21 and 11 in tmp:
        pos = tmp.index(11)
        tmp[pos] = 1

    return sum(tmp)


def show_hands(card_list, container):
    card_characters = [cards[c] for c in card_list]
    hands = ' '. join(card_characters)
    container.html(f'<p style="font-size: 64px; color: red;">{hands}</p>')


def set_buttons(start=False, hit=True, showdown=True):
    # デフォルトは最初期状態のボタン。スタートがオン、その他はオフ
    st.session_state.states_buttons['Start'] = start
    st.session_state.states_buttons['Hit'] = hit
    st.session_state.states_buttons['Showdown'] = showdown


def clicked_start():
    st.session_state.cards_deck = list(range(4 * 13))
    shuffle(st.session_state.cards_deck)

    st.session_state.cards_player = []
    st.session_state.cards_player.append(st.session_state.cards_deck.pop(0))
    st.session_state.cards_player.append(st.session_state.cards_deck.pop(0))

    st.session_state.cards_dealer = []

    set_buttons(True, False, False)

    score = calculate_score(st.session_state.cards_player)
    st.session_state.message = f'Your current hand: {score}.'


def clicked_hit():
    st.session_state.cards_player.append(st.session_state.cards_deck.pop(0))
    score = calculate_score(st.session_state.cards_player)
    st.session_state.message = f'Your current hand: {score}.'
    if score > 21:
        st.session_state.message = 'Player busted.'
        st.session_state.history['dealer'] += 1          # dealer の勝ち
        set_buttons()


def clicked_showdown():
    while calculate_score(st.session_state.cards_dealer) < 17:
        st.session_state.cards_dealer.append(st.session_state.cards_deck.pop(0))

    # ディーラがバストしたか確認
    score_dealer = calculate_score(st.session_state.cards_dealer)
    if score_dealer > 21:
        st.session_state.message = 'Dealer busted.'
        st.session_state.history['player'] += 1          # player の勝ち
        set_buttons()
        return

    score_player = calculate_score(st.session_state.cards_player)
    if score_player > score_dealer:
        win = 'Player won'
        st.session_state.history['player'] += 1          # player の勝ち
    elif score_player < score_dealer:
        win = 'Dealer won'
        st.session_state.history['dealer'] += 1          # dealer の勝ち
    else:
        win = 'Draw'
        st.session_state.history['draw'] += 1          # dealer の勝ち

    st.session_state.message = f'Player {score_player}, Dealer {score_dealer}. {win}.'
    set_buttons()


if 'cards_player' not in st.session_state:
    st.session_state.cards_player = []

if 'cards_dealer' not in st.session_state:
    st.session_state.cards_dealer = []

if 'message' not in st.session_state:
    st.session_state.message = 'Start the game from `Start` button.'

if 'states_buttons' not in st.session_state:
    st.session_state.states_buttons = {
        'Start': False,
        'Hit': True,
        'Showdown': True
    }

if 'history' not in st.session_state:
    st.session_state.history = {
        'player': 0,
        'dealer': 0,
        'draw': 0
    }


border_height = 250

container_dealer = st.container(border=True, height=border_height)
container_dealer.write('**Dealer**')
show_cards(st.session_state.cards_dealer, container_dealer)

container_player = st.container(border=True, height=border_height)
container_player.write('**Player**')
show_cards(st.session_state.cards_player, container_player)

container_console = st.container(border=True)
container_console.write(st.session_state.message)


st.sidebar.button('Start', disabled=st.session_state.states_buttons['Start'], on_click=clicked_start)
st.sidebar.button('Hit', disabled=st.session_state.states_buttons['Hit'], on_click=clicked_hit)
st.sidebar.button('Showdown', disabled=st.session_state.states_buttons['Showdown'], on_click=clicked_showdown)
st.sidebar.write(st.session_state.history)
