print("\n*****************************************************")
print("\n              Jogo da Advinhação")
print("\n*****************************************************")

num_secreto = 15

num_digitado = int(input('Digite um número: '))

if num_secreto == num_digitado:
    print('\nAcertou!')
else:
    print('\nErrou!')
