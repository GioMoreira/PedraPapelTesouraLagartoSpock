from random import randint
from time import sleep

cor = {'aqua': '\033[1;36m', 'verde': '\033[1;32m', 'azul': '\033[1;34m', 'lim': '\033[m'}

itens = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock')
computador = randint(0, 4)
print('''{}AS OPÇÕES SÃO:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
[ 3 ] LAGARTO
[ 4 ] SPOCK{}'''.format(cor['azul'], cor['lim']))
jogador = int(input('\033[1mQual sua jogada? \033[m'))
if jogador > 4:
    print('\033[1;31mJOGADA INVÁLIDA!\033[m')
else:
    print('{}!!!{}{}PedraPapelTesouraLagartoSPOCK{}{}!!!{}'.format(cor['aqua'], cor['lim'], cor['verde'], cor['lim'],
                                                                   cor['aqua'], cor['lim']))
    sleep(1)
    print('{}-={}'.format(cor['aqua'], cor['lim']) * 15)
    print('{}Você escoheu {}{}'.format(cor['azul'], itens[jogador], cor['lim']))
    print('{}O computador escolheu {}{}'.format(cor['azul'], itens[computador], cor['lim']))
    print('{}-={}'.format(cor['aqua'], cor['lim']) * 15)

    if computador == 0:  # computador jogou PEDRA
        if jogador == 0:
            print('\033[1mEMPATE!')
        elif jogador == 1:
            print('\033[1mVOCÊ VENCEU!! Papel embrulha Pedra.')
        elif jogador == 2:
            print('\033[1mO COMPUTADOR VENCEU! Pedra quebra Tesoura.')
        elif jogador == 3:
            print('\033[1mO COMPUTADOR VENCEU! Pedra esmaga Lagarto.')
        elif jogador == 4:
            print('\033[1mVOCÊ VENCEU!! Spock destrói Pedra.')

    elif computador == 1:  # computador jogou PAPEL
        if jogador == 0:
            print('\033[1mO COMPUTADOR VENCEU! Papel embrulha Pedra.')
        elif jogador == 1:
            print('\033[1mEMPATE!')
        elif jogador == 2:
            print('\033[1mVOCÊ VENCEU!! Tesoura corta Papel.')
        elif jogador == 3:
            print('\033[1mVOCÊ VENCEU!! Lagarto come Papel.')
        elif jogador == 4:
            print('\033[1mO COMPUTADOR VENCEU! Papel desmente Spock.')
    elif computador == 2:  # computador jogou TESOURA
        if jogador == 0:
            print('\033[1mVOCÊ VENCEU!!')
        elif jogador == 1:
            print('\033[1mO COMPUTADOR VENCEU!')
        elif jogador == 2:
            print('\033[1mEMPATE!')
        elif jogador == 3:
            print('\033[1mO COMPUTADOR VENCEU! Tesoura decapta Lagarto.')
        elif jogador == 4:
            print('\033[1mVOCÊ VENCEU!! Spock esmaga tesoura.')
    elif computador == 3:  # computador jogou LAGARTO
        if jogador == 0:
            print('\033[1mVOCÊ VENCEU!! Pedra esmaga Lagarto.')
        elif jogador == 1:
            print('\033[1mO COMPUTADOR VENCEU! Lagarto come Papel.')
        elif jogador == 2:
            print('\033[1mVOCÊ VENCEU!! Tesoura decapta Lagarto.')
        elif jogador == 3:
            print('\033[1mEMPATE!')
        elif jogador == 4:
            print('\033[1mO COMPUTADOR VENCEU! Lagarto envenena Spock.')
    elif computador == 4:  # computador jogou SPOCK
        if jogador == 0:
            print('\033[1mO COMPUTADOR VENCEU! Spock destrói Pedra.')
        elif jogador == 1:
            print('\033[1mVOCÊ VENCEU!! Papel desmente Spock.')
        elif jogador == 2:
            print('\033[1mO COMPUTADOR VENCEU!! Spock esmaga Tesoura.')
        elif jogador == 3:
            print('\033[1mVOCÊ VENCEU!! Lagarto envenena Spock')
        elif jogador == 4:
            print('\033[1mEMPATE!!')
