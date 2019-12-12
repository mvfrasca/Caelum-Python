
# Exercício 5.8 - pág. 55
def teste_args_kwargs(arg1, **kwargs):
    print(f'Argumento arg1 = {arg1}')
    for chave, valor in kwargs.items():
        print(f'Argumento {chave} = {valor}')

argumentos = {'nome': 'Marcelo', 'cpf': 11122233344}

print('\nOpção 1:')
teste_args_kwargs('1', **argumentos)
print('\nOpção 2:')
teste_args_kwargs('2', nome= 'Marcelo', cpf= 11122233344)
print('')
teste_args_kwargs('3', nome= 'Marcelo', cpf= 11122233344, idade=35)