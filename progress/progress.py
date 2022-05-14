import copy

def get_card(cards, board):
    tmp = copy.deepcopy(board)
    for card in cards:
        num, sym = map(str, card)
        if num.isnumeric():
            num = int(num)
            tmp[num].append(sym)
        else:
            face_card = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10}
            tmp[face_card[num]].append(sym)
            if num == 'A':
                tmp[1].append(sym)
    return tmp