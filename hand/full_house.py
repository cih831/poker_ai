# [triple, two_pair, kicker]
def full_house(cards):
    tri_cnt = 0
    two_cnt = 0
    pair = [0, 0, 0]    
    for i in range(14, 1, -1):
        if len(cards[i]) >= 3:
            pair[tri_cnt] = i
            tri_cnt += 1
        elif len(cards[i]) >= 2:
            if two_cnt >= 1:
                continue
            two_cnt += 1
            pair[1] = i
    if pair[0] and pair[1]:
        pair[2] = pair[1]
        return pair
    else:
        return False
