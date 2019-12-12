import random

# Inicialização
# palavras_secretas = ["banana", "acerola", "cupuaçu", "carambola", "uva", "melancia", "maça", "abacaxi", "coco", "tomate", "laranja"]
palavras_secretas = []
arquivo_palavras = open('palavras_forca.txt', 'r')
for linha in arquivo_palavras:
    fruta = linha.strip()
    palavras_secretas.append(fruta)

def jogar():
    palavra_secreta = palavras_secretas[random.randrange(0, len(palavras_secretas))]
    qtd_tentativas = 6
    qtd_erros = 0
    ganhou = False
    enforcou = False
    palavra_descoberta = ['_' for letra in palavra_secreta] # List comprehenSIOu
    # while len(palavra_descoberta) < len(palavra_secreta):
    #     palavra_descoberta.append("_")

    print("************************************************************")
    print("                     JOGO DA FORCA")
    print("************************************************************\n")

    # Loop do Jogo
    while (not ganhou and not enforcou):
        # Mostra a palavra descoberta até o momento
        print("\nPalavra secreta: {}".format(palavra_descoberta))
        print("\n")
        # Recupera o chute do usuário
        chute = input("Chute uma letra: ")
        # Verifica existência da letra na palavra
        if chute in palavra_descoberta:
            print("\nO fiiiii! Essa letra você já chutou!")
        elif chute in palavra_secreta:
            # Verifica as ocorrências da letra na palavra
            posicao = 0
            for letra in palavra_secreta:
                if chute.lower() == letra.lower():
                    palavra_descoberta[posicao] = letra
                posicao += 1
            print(f'Uhuuuuu a letra {chute.lower()} foi encontrada!')
        else:
            # Caso a letra não exista atualiza a qtd de erros
            qtd_erros += 1
            print("Xiiiii a letra {} não existe na palavra secreta!".format(chute))
            print("Você errou {} vezes de {} possíveis!".format(qtd_erros, qtd_tentativas))

        # Verifica se qtd de erros possíveis foi ultrapassada
        enforcou = qtd_erros == qtd_tentativas
        # Verifica se a palavra secreta foi descoberta
        ganhou =  '_' not in palavra_descoberta

    if ganhou:
        print("\n")
        print("              \o/")
        print("\nParabéns, você acertou a palavra secreta!\n")
    else:
        print("\nVocê se enforcou!\n")
