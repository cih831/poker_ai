def flush(hand):
    for pattern in 'sdhc':                                  # 문양 순회
        best5 = []
        for num in range(14, 1, -1):
            if pattern in hand[num]:                        # 문양이 핸드에 있으면 변수에 저장
                best5.append(num)
            if len(best5) == 5:
                return [6, best5]

    return False