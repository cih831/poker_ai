def loyal_straight_flush(hands):
    for pattern in 'sdhc':                  # 10 ~ A 문양이 전부 같으면
        for i in range(10, 15):
            if not pattern in hands[i]:
                break
        else:
            return [10, list(range(14, 9, -1))]
    return False