def full_house(cards):
    pair = []
    triple = []
    for i in range(14, 1, -1):
        if len(cards[i]) == 3 and not triple:
            triple = [i, i, i]

        elif len(cards[i]) >= 2 and not pair:
            pair = [i, i]

        if triple and pair:
            return [6, triple + pair]

    return False