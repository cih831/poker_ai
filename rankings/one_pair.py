# [one_pair, kicker]
def one_pair(cards):
    best5 = []
    for i in range(14, 1, -1):
        if len(cards[i]) == 2:
            best5.append(i)
            best5.append(i)
            break

    for i in range(14, 1, -1):
        if len(best5) == 5:
            break

    # if pair[0]:
    #     return pair
    # else:
    #     return False