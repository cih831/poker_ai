def loyal_straight_flush(hand):
    for pattern in 'sdhc':                  # 10 ~ A 문양이 전부 같으면
        if (pattern in hand[10] and
        pattern in hand[11] and
        pattern in hand[12] and
        pattern in hand[13] and
        pattern in hand[14]):
            return 'loyal_straight_flush'
    return False