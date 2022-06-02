def bet(player_lst, player_pot, player_state, player_balance, game, pre_flop=0):
    alive = 0
    for state in player_state:
        if state != 'fold':
            alive += 1

    while True:
        for pn in range(len(player_lst)):
            if (pre_flop):
                pn += 2
            pn = (pn + game) % len(player_lst)

            if player_state[pn] == 'fold':
                continue

            # check == 0, raise == 2.5(BB), call == -1, fold == -2
            if player_lst[pn] != 'hero':
                action = int(input())
            else:
                action = int(input())

            if action == -2:
                player_state[pn] = 'fold'
                alive -= 1
            elif action == -1:
                player_balance[pn] -= (max(player_pot) - player_pot[pn])
                player_pot[pn] = max(player_pot)
                player_state[pn] = 'call'
            elif action == 0:
                player_state[pn] = 'check'
            else:
                # 받고!
                player_balance[pn] -= (max(player_pot) - player_pot[pn])
                player_pot[pn] = max(player_pot)
                # 1억 더!
                player_balance[pn] -= action
                player_pot[pn] += action
                player_state[pn] = 'raise'
                for player_idx in range(len(player_state)):
                    if pn == player_idx:
                        continue
                    elif player_state[player_idx] == 'fold':
                        continue
                    else:
                        player_state[player_idx] = ''

            print(player_state)
            print(player_balance)

            if alive == 1:
                for pn in range(len(player_lst)):
                    if player_state[pn] != 'fold':
                        player_balance[pn] += sum(player_pot)
                return
            

        # 베팅 종료 확인
            for state in player_state:
                if not state:
                    break
            else:
                return
                


###########################################################
# player_lst = ['hero', 'cat', 'dog', 'apple', 'banana']
# player_pot = [2, 2, 2, 2, 2]
# player_state = ['', '', '', '', '']

# bet(player_lst, player_pot, player_state)
# print()
# print()
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print(player_lst)
# print(player_pot)
# print(player_state)
# print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
# print()
# print()

# bet(player_lst, player_pot, player_state)
# print(player_lst, player_pot, player_state)

# print(bet(player_lst, player_pot))
# print(player_lst, player_pot)
###########################################################