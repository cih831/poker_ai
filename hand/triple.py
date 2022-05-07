#[triple, kicker]
def triple(cards):
    cnt = 0
    pair = [0, 0]
    for i in range(14, 1, -1):
        if len(cards[i]) >= 3:
            cnt += 1
            pair[0] = i
            cards[i].pop()
            cards[i].pop()
            cards[i].pop()
            break

    for i in range(14, 1, -1):
        if len(cards[i]) >= 1:
            pair[1] = i
            break  
  
    if cnt >= 1:
        return pair
    else:
        return False    

