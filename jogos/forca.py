import random

def jogar():
    ''' 
    Função principal para iniciar o jogo da forca
    '''
    # Inicialização variáveis de controle
    qtd_tentativas = 6
    qtd_erros = 0
    ganhou = False
    enforcou = False
    # Inicialização palavras forca
    palavra_secreta = carrega_palavra_secreta()
    palavra_descoberta = inicializa_palavra_descoberta(palavra_secreta)
    letras_chutadas = []

    # Mostra mensagem de abertura
    imprime_mensagem_abertura()
    # Monta a tela
    imprime_tela(palavra_descoberta, letras_chutadas, qtd_erros, qtd_tentativas)

    # Loop do Jogo
    while (not ganhou and not enforcou):
        # Recupera o chute do usuário
        chute = pede_chute()
        # Verifica existência da letra na palavra

        if not valida_chute(chute, letras_chutadas):
            print('')
        elif chute in palavra_secreta:
            # Atualiza palavra descoberta com letra acertada
            palavra_descoberta = marca_chute_correto(chute, palavra_secreta, palavra_descoberta)
            letras_chutadas.append(chute)
            print(f'Uhuuuuu a letra {chute.lower()} foi encontrada!')
        else:
            # Caso a letra não exista atualiza a qtd de erros
            qtd_erros += 1
            letras_chutadas.append(chute)
            print("Xiiiii a letra {} não existe na palavra secreta!".format(chute))

        # Verifica se qtd de erros possíveis foi ultrapassada
        enforcou = qtd_erros == qtd_tentativas
        # Verifica se a palavra secreta foi descoberta
        ganhou =  '_' not in palavra_descoberta
        # Monta a tela
        imprime_tela(palavra_descoberta, letras_chutadas, qtd_erros, qtd_tentativas)

    if ganhou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


def imprime_mensagem_abertura():
    ''' 
    Imprime a mensagem de abertura
    '''
    print("************************************************************")
    print("                     JOGO DA FORCA")
    print("************************************************************\n")

def imprime_mensagem_vencedor():
    '''
    Imprime mensagem ao vencedor
    '''
    print("\n")
    print('Parabéns, você ganhou!')
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdedor(palavra_secreta):
    '''
    Imprime mensagem ao perdedor 
    '''
    print("\nVocê se enforcou!\n")
    print(f'A palavra era {palavra_secreta}')
    print("    _______________         ")
    print("   /               \        ")
    print("  /                 \       ")
    print("//                   \/\    ")
    print("\|   XXXX     XXXX   | /    ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/      ")
    print("   |\     XXX     /|        ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/        ")
    print("     \_         _/          ")
    print("       \_______/            ")

def imprime_tela(palavra_descoberta, letras_chutadas, qtd_erros, qtd_tentativas):
    '''
    Monta a tela do jogo
    '''
    print(" ______________________")
    print("|/                     |")
    if qtd_erros == 0:
        print("|                       ")
        print("|                       ")
        print("|                       ")
        print("|                       ")
        print("|                       ")
    elif qtd_erros == 1:
        print("|                      O")
        print("|                       ")
        print("|                       ")
        print("|                       ")
        print("|                       ")
    elif qtd_erros == 2:
        print("|                      O")
        print("|                      |")
        print("|                       ")
        print("|                       ")
        print("|                      ")
    elif qtd_erros == 3:
        print("|                      O")
        print("|                     /|")
        print("|                       ")
        print("|                       ")
        print("|                       ")
    elif qtd_erros == 4:
        print("|                      O ")
        print("|                     /|\ ")
        print("|                       ")
        print("|                       ")
        print("|                       ")
    elif qtd_erros == 5:
        print("|                      O ")
        print("|                     /|\ ")
        print("|                     / ")
        print("|                       ")
        print("|                       ")
    elif qtd_erros == 6:
        print("|                      0 ")
        print("|                     /|\ ")
        print("|      GAME OVER      / \ ")
        print("|                       ")
        print("|                       ")
    print("| ", end='')
    for letra in palavra_descoberta:
        print(f'{letra}  ', end='')
    print(f"\n\nLetras chutadas: {letras_chutadas}")
    print(f"Você errou {qtd_erros} vezes de {qtd_tentativas} possíveis!")


def carrega_palavra_secreta():
    ''' 
    Carrega a palavra a secreta a partir do arquivo de palavras secretas
    '''
    # palavras_secretas = ["banana", "acerola", "cupuaçu", "carambola", "uva", "melancia", "maça", "abacaxi", "coco", "tomate", "laranja"]
    palavras_secretas = []
    with open('palavras_forca.txt', 'r') as arquivo_palavras:
        for linha in arquivo_palavras:
            fruta = linha.strip()
            palavras_secretas.append(fruta)
    
    palavra_secreta = palavras_secretas[random.randrange(0, len(palavras_secretas))]
    return palavra_secreta


def inicializa_palavra_descoberta(palavra_secreta):
    '''
    Inicializa palavra descoberta completando a quantidade de letras da 
    palavra secreta com o caracter '_'
    '''
    # while len(palavra_descoberta) < len(palavra_secreta):
    #     palavra_descoberta.append("_")
    return ['_' for letra in palavra_secreta] # List comprehendion


def pede_chute():
    '''
    Recupera a letra do usuário
    '''
    chute = input("\nChute uma letra: ")
    chute = chute.strip().lower()
    return chute

def valida_chute(chute, letras_chutadas):
    '''
    Valida letra chutada
    '''
    if len(chute) > 1:
        print("\nInforme apenas uma letra")
    elif not chute.isalpha():
        print("\nInforme apenas letras (não números ou caracteres especiais)")
    elif chute in letras_chutadas:
        print("\nO fiiiii! Essa letra você já chutou!")
    else:
        return True
    return False

def marca_chute_correto(chute, palavra_secreta, palavra_descoberta):
    '''
    Atualiza a palavra_descoberta com a letra nas posições onde ela é 
    encontrada na palavra secreta
    '''
    # Verifica as ocorrências da letra na palavra
    posicao = 0
    for letra in palavra_secreta:
        if chute.lower() == letra.lower():
            palavra_descoberta[posicao] = letra
        posicao += 1
    
    return palavra_descoberta