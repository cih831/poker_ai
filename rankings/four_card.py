def four_card(cards):
    quad = []
    kicker = []
    for i in range(14, 1, -1):
        if len(cards[i]) == 4:
            quad = [i, i, i, i]

        elif cards[i] and not kicker:
            kicker.append(i)

        if len(quad + kicker) == 5:
            return [7, quad + kicker]

    return False