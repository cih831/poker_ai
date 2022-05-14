# [four_card, kicker]
def four_card(cards):
    quad = []
    kicker = []
    for i in range(14, 1, -1):
        if len(cards[i]) == 4:
            quad = [i, i, i, i]

        elif cards[i] and not kicker:
            kicker = [i]

        if quad and kicker:
            return [8, quad + kicker]

    return False