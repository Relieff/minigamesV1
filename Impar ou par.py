from random import randint
from time import sleep
import emoji

print('='*50)
print('Jogo de Impar ou Par'.center(50))
print('='*50)



sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(1)



print('Olá jogador, vamos jogar!')
print('-'*30)

while True:
    player = int(input('Escolha um número: '))
    computador = randint(0, 11) #O computador vai escolher algum desses números
    total = player + computador #O total vai ser os numeros do computador e do jogador
    tipo = ' ' #string vazia representado o que a pessoa vai escrever
    v = 0 #O 'V' é o número de vezes
    
    while tipo not in 'PpIi': #Enquanto o tipo não estiver dentro das strings 'PpIi' vai repetir a pergunta
        tipo = str(input('Par ou Impar?\n[P/I]: ')).strip().upper()[0]
    print(f'O jogador jogou {player} e o computador jogou {computador} e o total foi {total}')
    print('Deu par' if total %2 == 0 else 'Deu impar') #'Deu par' se o resto do total dividido por 2 for igual a 0 senao 'Deu impar'
    
    if tipo == 'P': #Se a resposta for P:
        if total % 2 == 0: #Se o resto do total dividido por 2 for igual a 0
            print(emoji.emojize('Você venceu! :check_mark:')) #O jogador ganha
            v += 1 #Pra mostrar o número de vezes que o jogador tentou
        else:
            print(emoji.emojize('Você perdeu! :cross_mark:'))
            break #Assim que o jogador perder o programa para
    
    elif tipo == 'I': #Se a resposta for I:
        if total % 2 == 1: #Se o resto do total dividido pro 2 for 1:
            print(emoji.emojize('Você venceu :check_mark:')) #O jogador perde
            v += 1
        else:
            print(emoji.emojize('Voce perdeu! :cross_mark:'))
            break
    print('Vamos jogar novamente . . .')
print('-'*40)
print(f'Gamer Over! Você venceu {v} vezes')
print(emoji.emojize('Fim do programa :Japanese_symbol_for_beginner:'))
print('-'*40)
