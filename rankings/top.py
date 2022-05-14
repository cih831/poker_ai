def top(cards):
    best5 = []
    for i in range(14, 1, -1):
        if cards[i]:
            best5.append(i)

        if len(best5) == 5:
            return [0, best5]