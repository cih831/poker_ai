from one_pair import one_pair
from two_pair import two_pair
from triple import triple
from straight import straight
from flush import flush
from full_house import full_house
from four_card import four_card
from straight_flush import straight_flush
from loyal_straight_flush import loyal_straight_flush

def rankings(hands):
    rank = [loyal_straight_flush, straight_flush, four_card, full_house, flush, straight, triple, two_pair, one_pair]
     
    for func in rank:
        value = func(hands)
        if value:
            return value
    best5 = []
    for i in range(14, 1, -1):
        if hands[i]:
            best5.append(i)
        
        if len(best5) == 5:
            return [0, best5]


# # top
# [[], ['s'], ['d'], [], ['h'], [], ['c'], [], ['d'], [], ['d'], [], ['h'], [], ['s']]

# # one-pair
# [[], ['d', 'c'], [], [], ['h'], [], ['c'], [], ['d'], [], ['d'], [], ['s'], [], ['d', 'c']]

# # two-pair
# [[], ['d', 'c'], [], [], ['h', 'c'], [], [], [], ['d'], [], ['d'], [], ['s'], [], ['d', 'c']]

# # triple
# [[], ['d', 'c', 'h'], [], [], [], [], ['c'], [], ['d'], [], ['d'], [], ['s'], [], ['d', 'c', 'h']]

# # straight
# [[], ['s'], ['d'], ['c'], ['h'], ['d'], [], [], [], [], ['d'], [], ['h'], [], ['s']]

# # flush
# [[], ['d'], ['d'], [], ['h'], [], ['d'], [], ['d'], [], ['d'], [], ['h'], [], ['d']]

# # full-house
# [[], ['d', 'c', 'h'], [], [], [], [], ['c', 's'], [], [], [], ['d'], [], ['s'], [], ['d', 'c', 'h']]

# # four-card
# [[], ['d', 'c', 'h', 's'], [], [], [], [], ['c'], [], [], [], ['d'], [], ['s'], [], ['d', 'c', 'h', 's']]

# # straight-flush
# [[], ['s'], ['s'], ['s'], ['s'], ['s'], [], [], [], [], ['d'], [], ['h'], [], ['s']]

# # loyal-straight-flush
# [[], ['s'], [], [], [], [], ['c'], [], ['d'], [], ['s'], ['s'], ['s'], ['s'], ['s']]