def vs(p1, p2):
    if p1[0] > p2[0]:
        return 1
    elif p1[0] < p2[0]:
        return -1
    else:
        for i in range(5):
            if p1[1][i] > p2[1][i]:
                return 1
            elif p1[1][i] < p2[1][i]:
                return -1

    return 0