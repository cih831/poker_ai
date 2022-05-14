def full_house(cards):
    pair = []
    triple = []
    for i in range(14, 1, -1):
        if len(cards[i]) >= 3:
            triple = [i, i, i]
        elif len(cards[i]) == 2:
            if pair:
                continue
            pair = [i, i]
    if triple and pair:
        return [7, triple + pair]
    else:
        return False