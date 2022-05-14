def straight_flush(cards):
    for pattern in 'sdhc':                              # 문양 순회
        best5 = []
        for i in range(14, 0, -1):
            if not cards[i] or not pattern in cards[i]:   # 숫자가 없거나 숫자에 문양이 없으면 cnt 초기화
                best5 = []
            else:
                best5.append(i)

            if len(best5) == 5:
                return [8, best5]

    return False