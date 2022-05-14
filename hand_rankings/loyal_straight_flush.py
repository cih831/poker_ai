def loyal_straight_flush(hands):
    print(hands)
    for pattern in 'sdhc':                  # 10 ~ A 문양이 전부 같으면
        if (pattern in hands[10] and
        pattern in hands[11] and
        pattern in hands[12] and
        pattern in hands[13] and
        pattern in hands[14]):
            return 'loyal_straight_flush'
    return False