# Inicialização
palavra_secreta = "banana"
qtd_tentativas = 7
qtd_erros = 0
ganhou = False
enforcou = False
palavra_descoberta = []
while len(palavra_descoberta) < len(palavra_secreta):
    palavra_descoberta.append("_")

while (not ganhou and not enforcou):
    # Recupera o chute do usuário
    chute = input("Chute uma letra: ")
    if chute in palavra_secreta:
        posicao = 0
        for letra in palavra_secreta:
            if chute.lower() == letra.lower():
                palavra_descoberta[posicao] = letra
            posicao += 1
    else:
        qtd_erros += 1

    print(palavra_descoberta)
    enforcou = qtd_erros == qtd_tentativas
    ganhou =  '_' not in palavra_descoberta

if ganhou:
    print("Parabéns, você acertou a palavra secreta!")
else:
    print("Você se enforcou danada!")