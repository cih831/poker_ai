def straight(hand):
    for i in range(1, 16):
        for j in range(i, i+5):
            if not hand[j]:
                break
        else:
            return 'straight'

hand = [[]*15]