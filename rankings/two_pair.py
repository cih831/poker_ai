def two_pair(cards):
    best5 = [2, []]

    for i in range(14, 1, -1):
        if len(best5[1]) >= 4:
            break
        if len(cards[i]) >= 2:
            best5[1].append(i)
            best5[1].append(i)
            
    if len(best5[1]) >= 4:
        for i in range(14, 1, -1):
            if len(cards[i]) == 1:
                best5[1].append(i)
                break
        return best5
    return False