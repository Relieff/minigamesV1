from random import randint
from time import sleep
import emoji

coresletras ={'branco':'\033[30m',     #Biblioteca de cores
              'limpa':'\033[m',
              'vermelho':'\033[31m',
              'verde':'\033[32m',
              'amarelo':'\033[33m',
              'azul':'\033[34m',
              'magenta':'\033[35m',
              'ciano':'\033[36m',
              'cinza':'\033[37m'}

tentativa = 0

p = str(input(emoji.emojize('Olá jogador, vamos fazer um jogo?:middle_finger: \n [S/N] '))).strip().upper()[0]

if p == 'S':
    print(emoji.emojize('Você escolheu o jogo! :check_mark:'))
    num = randint(1, 10)
    jogador = int(input(emoji.emojize('Pois bem jogador, entre 1 a 10 está o número que escolhi! Tente adivinhar! :grinning_squinting_face:  ')))
    
    while jogador != num:
        
        jogador = int(input('Tente novamente: '))
        
        
        if jogador == num:
            print(emoji.emojize('Woahh :face_with_open_mouth:  {}você conseguiu! Parabens!{}'.format(coresletras['magenta'], coresletras['limpa'])))
            tentativa += jogador

print('O jogador tentou {} vezes até conseguir!'.format(tentativa))

if p == 'N':
    print(emoji.emojize('Você escolheu sair! :cross_mark:'))
