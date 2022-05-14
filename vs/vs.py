def vs(p1, p2):
    print(type(p1))
    if p1[0] > p2[0]:
        return 'p1 win'
    elif p1[0] < p2[0]:
        return 'p2 win'
    else:
        for i in range(5):
            if p1[1][i] > p2[1][i]:
                return 'p1 win'
            elif p1[1][i] < p2[1][i]:
                return 'p2 win'

    return 'chop'