
def triple(cards):
    best5 = [3, []]
    for i in range(14, 1, -1):
        if len(cards[i]) == 3:
            best5[1].append(i)
            best5[1].append(i)
            best5[1].append(i)
            break

    temp = []
    for i in range(14, 1, -1):
        if len(temp) >= 2:
            break
        if len(cards[i]) == 1:
            temp.append(i)  
    best5[1] += temp

    if len(best5[1]) == 5:
        return best5
    return False    

