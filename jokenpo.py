import random
import os

def jokenpo (escolha_jogador):
    opcoes = ['Pedra','Papel','Tesoura']
    escolha_computador = random.choice(opcoes)

    print(f'Voce escolheu {escolha_jogador}')
    print(f'O Computador escolheu {escolha_computador}')

    if escolha_jogador == escolha_computador:
        return 'Empate !!!'
    elif (escolha_jogador == 'Pedra' and escolha_computador == 'Tesoura') or\
         (escolha_jogador == 'Papel' and escolha_computador == 'Pedra') or\
         (escolha_jogador == 'Tesoura' and escolha_computador == 'papel'):
            return 'Voce ganhou !!'
    else:
         return 'Voce perdeu'
cont = 'S'
while cont == 'S':
    print('Jokenpoooooooo!')
    print('_'*50)
    escolha_jogador = input('(Pedra, Papel, Tesoura ): ')
    escolha_jogador = escolha_jogador.capitalize()

    if escolha_jogador in ['Pedra','Papel','Tesoura']:
        resultado = jokenpo(escolha_jogador)
        print(resultado)
        cont = input('Voce quer continuar ? [S/N]: ')
        os.system('cls')
    else:
        print('Escolha Invalida !!!, escolha : Pedra, Papel ou Tesoura.')
print('Encerrando ......')