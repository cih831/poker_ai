import sys
sys.path.append('./rankings')
from rankings.rankings import rankings
from progress.progress import get_card


board = [[] for _ in range(15)]

# 히어로 패와 보드를 분리
# 족보 계산 할때 핸드를 더해서 계산


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

print(hero_ranking)
print(villain_ranking)