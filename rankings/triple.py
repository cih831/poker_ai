def triple(cards):
    tri = []
    kicker = []
    for i in range(14, 1, -1):
        if len(cards[i]) == 3:
            tri = [i, i, i]

        elif cards[i] and len(kicker) < 2:
            kicker.append(i)

        if len(tri + kicker) == 5:
            return [3, tri + kicker]

    return False

