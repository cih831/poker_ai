def one_pair(cards):
    pair = []
    kicker = []
    for i in range(14, 1, -1):
        if len(cards[i]) == 2:
            pair = [i, i]

        elif cards[i] and len(kicker) < 3:
            kicker.append(i)

        if len(pair + kicker) == 5:
            return [1, pair + kicker]
    
    return False