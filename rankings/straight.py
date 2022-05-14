def straight(hand):
    best5 = []
    for i in range(14, 0, -1):
        if not hand[i]:                 # 핸드 연결이 끊어지면 cnt 초기화
            best5 = []
        else:
            best5.append(i)
        
        if len(best5) == 5:
            return [5, best5]

    return False