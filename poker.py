def get_card(cards):
    global s, d, h, c
    for card in cards:
        num, sym = map(str, card)
        num = int(num)
        if sym == 's':
            s[num] += 1
        elif sym == 'd':
            d[num] += 1
        elif sym == 'h':
            h[num] += 1
        else:
            c[num] += 1

c = [[]*14]




hero_hands = list(map(str, input().split()))
get_card(hero_hands)
# print(s, d, h, c)

flop = list(map(str, input().split()))
get_card(flop)
# print(s, d, h, c)

turn = [input()]
print(turn)
get_card(turn)
# print(s, d, h, c)

river = [input()]
print(river)
get_card(river)