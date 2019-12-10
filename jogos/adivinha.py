print("*****************************************************")
print("              Jogo da Adivinhação")
print("*****************************************************")

# Inicialização
num_secreto = 15
num_tentativas = 0
rodada = 1

# Definição do nível
while (num_tentativas == 0):
    nivel = input("\nEm qual nível você deseja jogar (1, 2 ou 3): ")
    if nivel.isdigit():
        nivel = int(nivel)
    else:
        print("Informe um nível válido: 1, 2 ou 3")
        continue

    if nivel == 1:
        num_tentativas = 10
    elif nivel == 2:
        num_tentativas = 5
    elif nivel == 3:
        num_tentativas = 3
    else:
        print("\nInforme um nível válido: 1, 2 ou 3")

for rodada in range(1, num_tentativas + 1):
    print("\nTentativa {} do total de {} tentativas.".format(rodada, num_tentativas))

    # Recupera tentativa do usuário
    num_digitado = ""
    while not num_digitado.isdigit():
        num_digitado = input('\nDigite um número: ')
        if num_digitado.isdigit():
            num_digitado = int(num_digitado)
            break
        else:
            print("Informe um número inteiro válido")

    # Verificação
    acertou = num_digitado == num_secreto
    maior = num_digitado > num_secreto
    menor = num_digitado < num_secreto

    if acertou:
        print('\nAcertou! Número secreto: {}!'. format(num_secreto))
        break
    elif maior:
        print('\nO número informado ({}) é maior que o número secreto!'.format(num_digitado))
    elif menor:
        print('\nO número informado ({}) é menor que o número secreto!'.format(num_digitado))

    print("----------------------------------------")

if acertou:
    print("\nParabéns! Você acertou em {} tentativas!\n".format(rodada))
else:
    print("\nGAME OVER!\n")
    
