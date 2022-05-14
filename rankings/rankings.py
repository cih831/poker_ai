from top import top
from one_pair import one_pair
from two_pair import two_pair
from triple import triple
from straight import straight
from flush import flush
from full_house import full_house
from four_card import four_card
from straight_flush import straight_flush
from loyal_straight_flush import loyal_straight_flush

def rankings(cards):
    rank = [loyal_straight_flush, straight_flush, four_card, full_house, flush, straight, triple, two_pair, one_pair, top]
     
    for func in rank:
        value = func(cards)
        if value:
            return value


# # top
# [[], ['s'], ['d'], [], ['h'], [], ['c'], [], ['d'], [], ['d'], [], ['h'], [], ['s']]

# # one-pair
# [[], ['d', 'c'], [], [], ['h'], [], ['c'], [], ['d'], [], ['d'], [], ['s'], [], ['d', 'c']]

# # two-pair
# [[], ['d', 'c'], [], [], ['h', 'c'], [], [], [], ['d'], [], ['d'], [], ['s'], [], ['d', 'c']]
# [[], ['d', 'c'], [], [], ['h', 'c'], [], [], [], ['d', 'h'], [], [], [], ['s'], [], ['d', 'c']]

# # triple
# [[], ['d', 'c', 'h'], [], [], [], [], ['c'], [], ['d'], [], ['d'], [], ['s'], [], ['d', 'c', 'h']]

# # straight
# [[], ['s'], ['d'], ['c'], ['h'], ['d'], [], [], [], [], ['d'], [], ['h'], [], ['s']]

# # flush
# [[], ['d'], ['d'], [], ['h'], [], ['d'], [], ['d'], [], ['d'], [], ['h'], [], ['d']]

# # full-house
# [[], ['d', 'c', 'h'], [], [], ['c', 's'], [], ['c', 's'], [], [], [], ['d'], [], ['s'], [], ['d', 'c', 'h']]
# [[], ['d', 'c', 'h'], [], [], [], [], ['c', 's', 'h'], [], [], [], [], [], ['s'], [], ['d', 'c', 'h']]
# [[], ['d', 'c', 'h'], [], [], [], [], ['c', 's'], [], [], [], ['d', 's', 'h'], [], [], [], ['d', 'c']]
# [[], ['d', 'c', 'h'], [], [], [], [], ['c', 's', 'h'], [], [], [], ['d', 's'], [], [], [], ['d', 'c']]

# # four-card
# [[], ['d', 'c', 'h', 's'], [], [], [], [], ['c'], [], [], [], ['d'], [], ['s'], [], ['d', 'c', 'h', 's']]

# # straight-flush
# [[], ['s'], ['s'], ['s'], ['s'], ['s'], [], [], [], [], ['d'], [], ['h'], [], ['s']]

# # loyal-straight-flush
# [[], ['s'], [], [], [], [], ['c'], [], ['d'], [], ['s'], ['s'], ['s'], ['s'], ['s']]