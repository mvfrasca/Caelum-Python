# ************************************************************************
#                                Funções                                 #
# ************************************************************************

# Exercício 5.2 - pág. 52

def velocidade_media(distancia, tempo):
    return divisao(distancia, tempo)

def soma(valor1, valor2):
    return valor1 + valor2

def subtracao(valor1, valor2):
    return valor1 - valor2

def multiplicacao(valor1, valor2):
    return valor1 * valor2

def divisao(valor1, valor2):
    ''' Divide o valor1 pelo valor2 '''
    return valor1 / valor2

def calculadora(valor1, valor2):
    vl_soma = soma(valor1, valor2)
    vl_subtracao = subtracao(valor1, valor2)
    vl_multiplicacao = multiplicacao(valor1, valor2)
    vl_divisao = divisao(valor1, valor2)
    return {
        'soma': vl_soma,
        'subtracao': vl_subtracao,
        'multiplicacao': vl_multiplicacao,
        'divisao': vl_divisao
    }

# Testes
valor1 = int(input('\nInforme o valor 1: '))
valor2 = int(input('Informe o valor 2: '))
print(f'Resultado velocidade média: {velocidade_media(valor1,valor2)}')
print(f'Resultado calculadora: {calculadora(valor1,valor2)}\n')
