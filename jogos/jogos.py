import adivinha
import forca

def jogar():
    print('***********************************************************')
    print('                     JOGOS PYTHON')
    print('***********************************************************')
    print('\n1 - Jogo da Advinhação')
    print('2 - Jogo da Forca')
    escolha = ''
    while escolha not in ('1','2'):
        escolha = input('\nEscolha o jogo: ')

    if escolha == '1':
        adivinha.jogar()
    elif escolha == '2':
        forca.jogar()

jogar()