import random
import pygame
print('-='*50)
print('\nPergunta \033[7;31;40mR\033[7;32;40mG\033[7;34;40mB\033[m do charada\n')
print('\033[7;32;40m{:^100}\033[m\n'.format('?'))
print('-='*50)
print('Você terá apenas uma dica para acertar as duas cores!\n')
print('Dica    \033[7;32;40m?\033[m')
n1 = random.randint(0, 2)
n2 = random.randint(0, 2)
if n1 < 1: #azul
    if n2 == 0:
        d = 'Qual a semelhança entre luz da insonia e um céu sem nuvens?'
    else:
        if n2 == 1:
            d = 'Como as veias se parecem diferentes quando sob a pele!'
        else:
            d = 'A menor parte do planeta terra e a maior parte do planeta...'
else:
    if n1 > 1: #verde
        if n2 == 0:
            d = 'A maior parte do planeta terra e a menor parte do planeta...'
        else:
            if n2 == 1:
                d = 'No primeiro sinal você para, no segundo voce segue...'
            else:
                d = 'O que seria do charada se ele não pudesse VER DE perto?'
    else: #vermelho
        if n2 == 0:
            d = 'O céu ao por do sol na praia é muito bonito, não acha?'
        else:
            if n2 == 1:
                d = 'Qual a cor do liquido que você não deve beber, mas não pode viver sem?'
            else:
                d = 'Como se chama quando um morango não está maduro?'
print(d)
pygame.init()
pygame.mixer.music.load('riddle.ogg')
pygame.mixer.music.play()
x2 = input('\nQual cor será escrita? ').lower()
x1 = input('\nE qual vai ser a cor do texto? ').lower()
print()
l1 = ['\033[34m', '\033[31m', '\033[32m']
l2 = ['azul', 'vermelho', 'verde']
v1 = l1[n1]
v2 = l2[n2]
y = '{}{}'.format(v1, v2)
r1 = 'Você acertou, a resposta era {}\033[m você deve ter roubado...'.format(y)
r2 = 'Você acertou a cor escrita mas errou a cor do texto, a resposta era {}\033[m.'.format(y)
r3 = 'Você errou a cor escrita mas acertou a cor do texto, a resposta era {}\033[m.'.format(y)
r4 = 'Você errou as duas respostas, a resposta certa era {}\033[m.'.format(y)
if n1 != 0:
    if n1 != 1:
        c = 'verde'
    else:
        c = 'vermelho'
else:
    c = 'azul'
if x1 == c and x2 == v2:
    print(r1)
    u = 1
else:
    u = 0
    if x1 != c and x2 == v2:
        print(r2)
    else:
        if x1 == c and x2 != v2:
            print(r3)
        else:
            print(r4)
if u == 1:
    print('\nParabens, \033[31m possível ladrão(a)!\033[m\n')
else:
    print('\nMais sorte da proxima \033[7;32;40m HAHAHAHA\033[m.\n')
print('\033[7;32;40m{:^100}\033[m\n'.format('?'))
