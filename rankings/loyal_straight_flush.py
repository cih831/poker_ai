def loyal_straight_flush(cards):
    for pattern in 'sdhc':                  # 10 ~ A 문양이 전부 같으면
        for i in range(10, 15):
            if not pattern in cards[i]:
                break
        else:
            return [9, [14, 13, 12, 11, 10]]
    return False