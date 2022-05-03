# JAN KEN PO game :: github.com/sliatecinos
# _*_ coding: utf-8 _*_
from random import randint
from time import sleep


def jogo_start():
    n_jogadas=0
    opt = [" ROCK \U0001F311"," PAPER \U0001F4DC",' SCISSORS \U00002702']
    pts_computer=0
    pts_player=0

    while True:
        header=' | '.join(['['+str(opt.index(i))+']'+i for i in opt])
        print(f'{"="*44}\n{header}\n{"="*44}')
        computer=randint(0,2)
        player=input('Choose Your Weapon [3 or more to stop]: ')

        if player not in '012':
            break
        else:
            n_jogadas += 1

        player=int(player)
        jankenpon = ['JAN','KEN','PON!!!']
        for i in jankenpon:
            sleep(.6)
            print(f'-{i}...')
        sleep(1.)

        if computer - player == 1 or computer - player == -2:
            print(f'\nCOMPUTER wins\t:[{computer}]-{opt[computer]}\nYOU lose\t:[{player}]-{opt[player]}\n')
            pts_computer += 1
        elif player - computer == 1 or player - computer == -2:
            print(f'\nCOMPUTER loses\t:[{computer}]-{opt[computer]}\nYOU win\t:[{player}]-{opt[player]}\n')
            pts_player += 1
        else:
            print(f'\nDRAW!!\nCOMPUTER\t:[{computer}]-{opt[computer]}\nYOU      \t:[{player}]-{opt[player]}\n')

        print('*'*3,' NOW PLAY AGAIN !!! ','*'*3,sep='')

    if pts_player > 0:
        print(f'{n_jogadas} games played in total.')
        print(f'Computer won \t{pts_computer} times.')
        print(f'You won \t{pts_player} times.')
    else:
        print('YOU HAVE NOT PLAYED YET... \U0001F615')

print('*'*8,'LETS GO PLAY \'JAN-KEN-PON\'','*'*8)
jogo_start()
