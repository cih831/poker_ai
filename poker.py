import sys
sys.path.append('./rankings')
from rankings.rankings import rankings
from progress.progress import get_card
from vs.vs import vs
from bet.bet import bet

blind, hero_balance, villain_balance = map(int, input().split())
hero_balance /= blind
villain_balance /= blind
BB = 0

board = [[] for _ in range(15)]
hero_pot = villain_pot = 0
# pot == hero_pot + villain_pot

hero_hands = list(map(str, input().split()))
# result = bet(
    # 순서에 따라 상대 베팅 내 베팅 하는데
    # 내 베팅에 ai 동작하게끔?
# )

flop = list(map(str, input().split()))
board = get_card(flop, board)
hero_ranking = rankings(get_card(hero_hands, board))
# bet(누가 먼저 베팅?, hero_ranking, board, 여태 상대가 했던 베팅 라인을 넣어주면 판단하기 쉬울듯..?, 게임 계속 진행하면서 상대방에 대한 데이터 수집해서 공격적인 성향인지 수비적인지 판단하는 인자)


turn = [input()]
board = get_card(turn, board)
hero_ranking = rankings(get_card(hero_hands, board))
# bet()


river = [input()]
board = get_card(river, board)
hero_ranking = rankings(get_card(hero_hands, board))
# bet()

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