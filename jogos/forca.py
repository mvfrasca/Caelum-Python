import random

# Inicialização
palavra_secreta = "banana"
qtd_tentativas = 7
qtd_erros = 0
ganhou = False
enforcou = False
palavra_descoberta = []
while len(palavra_descoberta) < len(palavra_secreta):
    palavra_descoberta.append("_")

print("************************************************************")
print("                     JOGO DA FORCA")
print("************************************************************\n")

# Loop do Jogo
while (not ganhou and not enforcou):
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
        print("Uhuuuuu a letra {} foi encontrada!".format(letra))
    else:
        # Caso a letra não exista atualiza a qtd de erros
        qtd_erros += 1
        print("Xiiiii a letra {} não existe na palavra secreta!".format(letra))
        print("Você errou {} vezes de {} possíveis!".format(qtd_erros, qtd_tentativas))

    # Mostra a palavra descoberta até o momento
    print("\n {}".format(palavra_descoberta))
    print("\n")
    # Verifica se qtd de erros possíveis foi ultrapassada
    enforcou = qtd_erros == qtd_tentativas
    # Verifica se a palavra secreta foi descoberta
    ganhou =  '_' not in palavra_descoberta

if ganhou:
    print("              \o/")
    print("\n")
    print("\nParabéns, você acertou a palavra secreta!\n")
else:
    print("\nVocê se enforcou!\n")
