def bet(player_lst, player_pot):
    while True:
        for pn in range(2, len(player_lst)+2):
            pn %= len(player_lst)
            if player_lst[pn] != 'hero':
                action = 0
            else:
                action = int(input())
            if action == -2:
                player_pot[pn] *= -1
            elif action == -1:
                player_pot[pn] = max(player_pot)
            else:
                player_pot[pn] += action

            # 베팅 종료 확인
            for pp in player_pot:
                if pp >= 0:
                    tmp = pp
                    break
            for pp in player_pot:
                if pp >= 0 and pp != tmp:
                    break
            else:
                return player_pot