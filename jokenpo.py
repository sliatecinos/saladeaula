# _*_ coding: utf-8 _*_
from random import randint
from time import sleep


def jogo_start():
    n_jogadas=0
    opt = [" ROCK \N{Rock}"," PAPER \N{Scroll}",' SCISSORS \N{Black Scissors}']
    pts_computer=0
    pts_player=0

    while True:
        n_jogadas += 1
        header=' | '.join(['['+str(opt.index(i))+']'+i for i in opt])
        print(f'{"="*44}\n{header}\n{"="*44}')
        computer=randint(0,2)
        player=input('Choose Your Weapon: ')

        if player not in '012':
            print(f'{n_jogadas} games played in total.')
            print(f'Computer won \t{pts_computer} times.')
            print(f'You won \t{pts_player} times.')
            break
        player=int(player)
        sleep(1)
        print('-JAN...')
        sleep(1)
        print('-KEN...')
        sleep(1)
        print('-PON!!...\n')
        sleep(1.5)

        if computer - player == 1 or computer - player == -2:
            print(f'COMPUTER wins\t:[{computer}]-{opt[computer]}\nYOU lose\t:[{player}]-{opt[player]}')
            pts_computer += 1
        elif player - computer == 1 or player - computer == -2:
            print(f'COMPUTER loses\t:[{computer}]-{opt[computer]}\nYOU win\t:[{player}]-{opt[player]}')
            pts_player += 1
        else:
            print(f'DRAW!!\nCOMPUTER\t:[{computer}]-{opt[computer]}\nYOU      \t:[{player}]-{opt[player]}')


        print('*'*3,' NOW PLAY AGAIN !!! ','*'*3,sep='')


print('*'*8,'LETS GO PLAY \'JAN-KEN-PON\'','*'*8)
jogo_start()
