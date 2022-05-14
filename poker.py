import sys
sys.path.append('./hand_rankings')
from hand_rankings.hand_rankings import rankings
from progress.progress import get_card


hands = [[] for _ in range(15)]


hero_hands = list(map(str, input().split()))
get_card(hero_hands, hands)

flop = list(map(str, input().split()))
get_card(flop, hands)

turn = [input()]
get_card(turn, hands)

river = [input()]
get_card(river, hands)

print(rankings(hands))