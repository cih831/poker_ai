def flush(hand):
    for pattern in 'sdhc':                                  # 문양 순회
        flush_top5 = []
        for num in range(2, 15):
            if pattern in hand[num]:                        # 문양이 핸드에 있으면 변수에 저장
                flush_top5.append(num)
        if len(flush_top5) >= 5:                            # 변수에 카드가 5장 이상 쌓였으면
            return f'{flush_top5[-5:]} flush'               # 제일 큰 다섯장만 뽑아내서 리턴
    return False

hand = [[], ['s'], ['d'], [], [], ['d', 'h'], [], ['d'], ['d'], [], ['d'], [], [], [], ['s']]

print(flush(hand))