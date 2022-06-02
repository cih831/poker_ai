# 내가 레이즈 = > 상대 레이즈 = > 나 레이즈 => 상대 레이즈

# 내가 죽거나, 상대가 죽거나, pot에 얼마 추가되었는지
# if hero fold => return villain win
# elif villain fold => return hero win
# elif check check => return (raise amount(==0))
# elif raise call => return (raise amount)

# 리스트가 idx가 key이고 value인 딕셔너리랑 비슷한 구조니까

# player_lst == [hero, villain1, villain2, villain3]
# player_pot == [0, 0, 0, 0]
def bet(player_lst, player_pot):
    while True:
        for pn in range(len(player_lst)):
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
                
            # check == 0, raise == 2.5(BB), call == -1, fold == -2