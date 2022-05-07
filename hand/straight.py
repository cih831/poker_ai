def straight(hand):
    for i in range(1, 16):
        for j in range(i, i+5):
            if not hand[j]:
                break
        else:
            return f'{hand[j+4]} straight'
    return False

hand = [[], ['s'], ['d'], ['c'], ['h'], ['d'], [], [], [], [], ['d'], [], ['h'], [], ['s']]

print(straight(hand))