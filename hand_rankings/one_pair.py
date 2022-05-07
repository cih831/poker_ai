# [one_pair, kicker]
def one_pair(cards):
    pair = [0, 0]
    for i in range(14, 1, -1):
        if len(cards[i]) == 2:
            pair[0] = i
            break

    for i in range(14, 1, -1):
        if len(cards[i]) == 1:
            pair[1] = i
            break

    if pair[0]:
        return pair
    else:
        return False