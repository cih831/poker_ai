def two_pair(cards):
    pair1 = []
    pair2 = []
    kicker = []

    for i in range(14, 1, -1):
        if len(cards[i]) == 2:
            if not pair1:
                pair1 = [i, i]

            elif not pair2:
                pair2 = [i, i]

        elif cards[i] and not kicker:
            kicker.append(i)
        
        if len(pair1 + pair2 + kicker) == 5:
            return [2, pair1 + pair2 + kicker]

    return False