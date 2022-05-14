def get_card(cards, hands):
    for card in cards:
        num, sym = map(str, card)
        if num.isnumeric():
            num = int(num)
            hands[num].append(sym)
        else:
            face_card = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
            hands[face_card[num]].append(sym)
            if num == 'A':
                hands[1].append(sym)