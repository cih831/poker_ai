import sys
sys.path.append('./rankings')
from rankings.rankings import rankings
from progress.progress import get_card
from vs.vs import vs
from bet.bet import bet

blind = int(input())
player_balance = list(map(lambda x: (int(x)/blind), input().split()))
player_lst = ['hero', 'villain']
game = -1

while True:
    game += 1
    board = [[] for _ in range(15)]
    player_pot = [0, 0]
    player_state = ['', '']


    hero_hands = list(map(str, input().split()))
    if hero_hands == ['-1', '-1']:
        break

    if bet(player_lst, player_pot, player_state, player_balance, game, 1):
        continue

    # print(player_state)
    # print(player_pot)

    flop = list(map(str, input().split()))
    board = get_card(flop, board)
    hero_ranking = rankings(get_card(hero_hands, board)) # 이거 나중에 bet 인자로 ai 판단 근거로 줘야됨
    if bet(player_lst, player_pot, player_state, player_balance, game):
        continue



    turn = [input()]
    board = get_card(turn, board)
    hero_ranking = rankings(get_card(hero_hands, board))
    if bet(player_lst, player_pot, player_state, player_balance, game):
        continue


    river = [input()]
    board = get_card(river, board)
    hero_ranking = rankings(get_card(hero_hands, board))
    if bet(player_lst, player_pot, player_state, player_balance, game):
        continue

    for pn in range(len(player_lst)):
        if player_lst[pn] == 'hero':
            player_state[pn] = hero_ranking
            continue
        if player_state[pn] == 'fold':
            player_state[pn] = [-1, []]
            continue
        villain_hands = list(map(str, input().split()))
        player_state[pn] = rankings(get_card(villain_hands, board))
    
    print(player_state)
        
    # 1등 찾기
    tmp = 0
    for pn in range(len(player_lst)):
        if vs(player_state[tmp], player_state[pn]) == -1:
            tmp = pn
    
    winner = []
    for pn in range(len(player_lst)):
        if player_state[tmp] == player_state[pn]:
            winner.append(pn)

    reward = sum(player_pot)/len(winner)
    for pn in winner:
        player_balance[pn] += reward

    print(player_balance)
    


    # print(hero_ranking, villain_ranking)
    # print(vs(hero_ranking, villain_ranking))



#################################################################################
# bet(누가 먼저 베팅?, hero_ranking, board, 여태 상대가 했던 베팅 라인을 넣어주면 판단하기 쉬울듯..?, 게임 계속 진행하면서 상대방에 대한 데이터 수집해서 공격적인 성향인지 수비적인지 판단하는 인자)

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
##################################################################################