# 높은 순으로
# [pair, pair, kicker]
def two_pair(cards):
    cnt = 0
    pair = [0, 0, 0]
    for i in range(14, 1, -1):
        if cnt >= 2:
            break

        if len(cards[i]) >= 2:
            pair[cnt] = i
            cnt += 1
            cards[i].pop()
            cards[i].pop()

    for i in range(14, 1, -1):
        if len(cards[i]) >= 1:
            pair[2] = i
            break

    if cnt >= 2:
        return pair
    else:
        return False
