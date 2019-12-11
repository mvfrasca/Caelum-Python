# Exercício 4.5 - pág 47

##################################################################################
# 1) Dada a lista:
##################################################################################
lista = [12,-2,4,8,29,45,78,36,-17,2,12,8,3,3,-52]
print(f'\n1) Dada a lista: {lista}')

# a) Imprima o maior elemento
print(f'a) Maior elemento: {max(lista)}')

# b) Imprima o menor elemento
print(f'b) Menor elemento: {min(lista)}')

# c) Imprima os números pares
pares = []
for e in lista:
    if e % 2 == 0:
        pares.append(e) 
print(f'c) Números pares: {pares}')

# d) Imprima o número de ocorrências do primeiro elemento da lista
num_elementos = 0
for e in lista:
    if e == lista[0]:
        num_elementos += 1 
print(f'd) Ocorrências do 1º elemento: {num_elementos} ou 2ª opção: {lista.count(lista[0])}')

# e) Imprima a médias dos elementos
soma = 0
for e in lista:
    soma += e
media = soma / len(lista)
# OU diretamente:
media = sum(lista) / len(lista)
print(f'e) Média elementos: {media}')

# f) Imprima a soma dos elementos de valor negativo
soma = 0
for e in lista:
    if e < 0:
        soma += e 
print(f'f) Soma dos elementos de valor negativo: {soma}')

##################################################################################
# 2) Faça um programa que leia dados do usuário  (nome, sobrenome, idade) 
# adicione em uma lista e imprima seus elementos na tela
##################################################################################
print('\n2) Faça um programa que leia dados do usuário  (nome, sobrenome, idade) adicione em uma lista e imprima seus elementos na tela')
# nome = input("Informe seu nome: ")
# sobrenome = input("Informe seu sobrenome: ")
# idade = input("Informe sua idade: ")
nome = ('nome', input("Informe seu nome: "))
sobrenome = ('sobrenome', input("Informe seu sobrenome: "))
idade = ('idade', input("Informe sua idade: "))
lista = [nome, sobrenome, idade]
print(f'Dados do usuário: {lista}')

##################################################################################
# 3) Faça um programa que leia 4 notas, mostre as notas e a média na tela
##################################################################################
print('\n3) Faça um programa que leia 4 notas, mostre as notas e a média na tela')
notas = []
soma = 0.0
for num_nota in range(1, 5):
    nota = input(f'Informe a nota nº {num_nota}: ')
    soma += float(nota)
    notas.append(nota)
media = soma / len(notas)
print(f'Notas: {notas}\nMédia: {media}')

##################################################################################
# 4) Faça um programa utilizando um dict que leia dados de entrada do usuário.
# O usuário deve entrar com os dados de uma pessoa como nome, idade e cidade onde
# mora. Após isso, você deve imprimir os dados como exemplo:
# nome: João
# idade: 20
# cidade: São Paulo
##################################################################################
print('\n4) Faça um programa utilizando um dict que leia dados de entrada do usuário. O usuário deve entrar com os dados de uma pessoa como nome, idade e cidade onde mora. Após isso, você deve imprimir os dados como exemplo:')
print('nome: João')
print('idade: 20')
print('cidade: São Paulo\n')
nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
idade = input("Informe sua idade: ")
cidade = input("Informe a cidade onde mora: ")
dicionario = {
    'nome': nome,
    'sobrenome': sobrenome,
    'idade': idade, 
    'cidade': cidade
}
print(f'\nDados do usuário:')
for chave, valor in dicionario.items():
    print(f'{chave}: {valor}')


##################################################################################
# 5) A partir no exercício anterior adicione a pessoa em uma lista. Pergunte ao
# usuário se ele deseja adicionar uma nova pessoa. Após adicionar dados de algumas
# pessoas, imprimir todos os dados de cada pessoa de forma organizada.
##################################################################################
print('\n5) A partir no exercício anterior adicione a pessoa em uma lista. Pergunte ao usuário se ele deseja adicionar uma nova pessoa. Após adicionar dados de algumas pessoas, imprimir todos os dados de cada pessoa de forma organizada.')

lista_pessoas = []
resp_usuario = ""

while resp_usuario in ['s','sim','']:
    resp_usuario = ''
    nome = input("Informe seu nome: ")
    sobrenome = input("Informe seu sobrenome: ")
    idade = input("Informe sua idade: ")
    cidade = input("Informe a cidade onde mora: ")
    pessoa = {
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': idade, 
        'cidade': cidade
    }
    lista_pessoas.append(pessoa)

    while resp_usuario.lower() not in ['s','n','sim','não']:
        resp_usuario = input('\nDeseja incluir uma nova pessoa na lista (S ou N)')

# Ordena a lista
lista_pessoas.sort(key=lambda p: p['nome'])
# Mostra as pessoas da lista
for pessoa in lista_pessoas:
    print(f'\nDados do usuário:')
    for chave, valor in pessoa.items():
        print(f'{chave}: {valor}')