import sys
sys.path.append('./rankings')
from rankings.rankings import rankings
from progress.progress import get_card
from vs.vs import vs


board = [[] for _ in range(15)]

hero_hands = list(map(str, input().split()))

flop = list(map(str, input().split()))
board = get_card(flop, board)
hero_ranking = rankings(get_card(hero_hands, board))

turn = [input()]
board = get_card(turn, board)
hero_ranking = rankings(get_card(hero_hands, board))


river = [input()]
board = get_card(river, board)
hero_ranking = rankings(get_card(hero_hands, board))

villain_hands = list(map(str, input().split()))
villain_ranking = rankings(get_card(villain_hands, board))

print(hero_ranking, villain_ranking)
print(vs(hero_ranking, villain_ranking))



# print(rankings([[], ['s'], ['d'], [], ['h'], [], ['c'], [], ['d'], [], ['d'], [], ['h'], [], ['s']]))                           # top
# print(rankings([[], ['d', 'c'], [], [], ['h'], [], ['c'], [], ['d'], [], ['d'], [], ['s'], [], ['d', 'c']]))                    # one pair
# print(rankings([[], ['d', 'c'], [], [], ['h', 'c'], [], [], [], ['d'], [], ['d'], [], ['s'], [], ['d', 'c']]))                  # two pair
# print(rankings([[], ['d', 'c'], [], [], ['h', 'c'], [], [], [], ['d', 'h'], [], [], [], ['s'], [], ['d', 'c']]))                # two pair
# print(rankings([[], ['d', 'c', 'h'], [], [], [], [], ['c'], [], ['d'], [], ['d'], [], ['s'], [], ['d', 'c', 'h']]))             # triple
# print(rankings([[], ['s'], ['d'], ['c'], ['h'], ['d'], [], [], [], [], ['d'], [], ['h'], [], ['s']]))                           # straight
# print(rankings([[], ['d'], ['d'], [], ['h'], [], ['d'], [], ['d'], [], ['d'], [], ['h'], [], ['d']]))                           # flush
# print(rankings([[], ['d', 'c', 'h'], [], [], ['c', 's'], [], ['c', 's'], [], [], [], ['d'], [], ['s'], [], ['d', 'c', 'h']]))   # full house
# print(rankings([[], ['d', 'c', 'h'], [], [], [], [], ['c', 's', 'h'], [], [], [], [], [], ['s'], [], ['d', 'c', 'h']]))         # full house
# print(rankings([[], ['d', 'c', 'h'], [], [], [], [], ['c', 's'], [], [], [], ['d', 's', 'h'], [], [], [], ['d', 'c']]))         # full house
# print(rankings([[], ['d', 'c', 'h'], [], [], [], [], ['c', 's', 'h'], [], [], [], ['d', 's'], [], [], [], ['d', 'c']]))         # full house
# print(rankings([[], ['d', 'c', 'h', 's'], [], [], [], [], ['c'], [], [], [], ['d'], [], ['s'], [], ['d', 'c', 'h', 's']]))      # four cards
# print(rankings([[], ['s'], ['s'], ['s'], ['s'], ['s'], [], [], [], [], ['d'], [], ['h'], [], ['s']]))                           # straight flush
# print(rankings([[], ['s'], [], [], [], [], ['c'], [], ['d'], [], ['s'], ['s'], ['s'], ['s'], ['s']]))                           # loyal straight flush