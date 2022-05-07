def straight_flush(hand):
    for pattern in 'sdhc':                              # 문양 순회
        cnt = 0
        high_card = 0
        for i in range(1, 15):
            if not hand[i] or not pattern in hand[i]:   # 숫자가 없거나 숫자에 문양이 없으면 cnt 초기화
                cnt = 0
            else:
                cnt += 1

            if cnt >= 5:                                # 5장 이상 모이면 high_card 설정
                high_card = i

        if high_card:                                   # for 문 끝나고 straight_flush 조건이 완성되면 리턴
            return f'{high_card} straight_flush'
    return False

hand = [[], ['d'], ['d'], ['d'], ['d'], ['d'], ['d'], [], [], [], [], [], ['h'], [], ['d']]

print(straight_flush(hand))