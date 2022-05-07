def straight(hand):
    cnt = 0
    high_card = 0
    for i in range(1, 15):
        if not hand[i]:                 # 핸드 연결이 끊어지면 cnt 초기화
            cnt = 0
        else:
            cnt += 1
        
        if cnt >= 5:                    # 다섯장 이상이면 하이카드를 바꿔줌
            high_card = i
        
    if high_card:
        return f'{high_card} straight'
    return False

hand = [[], ['s'], ['d'], ['c'], ['h'], ['d'], ['h'], [], [], [], [], [], ['h'], [], ['s']]

print(straight(hand))