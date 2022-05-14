def straight(cards):
    best5 = []
    for i in range(14, 0, -1):
        if not cards[i]:                 # 핸드 연결이 끊어지면 cnt 초기화
            best5 = []
        else:
            best5.append(i)
        
        if len(best5) == 5:
            return [4, best5]

    return False