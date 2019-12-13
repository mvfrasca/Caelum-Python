
def cria_conta(numero, titular, saldo, limite):
    '''
    Cria uma nova conta bancária
    '''
    conta = {'numero': numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta

def deposita(conta, valor):
    '''
    Realiza um depósito acrescentando o valor informado ao saldo da conta
    '''
    conta['saldo'] += valor

def saca(conta, valor):
    '''
    Realiza um saque deduzindo o valor informado do saldo da conta
    '''
    conta['saldo'] -= valor

def extrato(conta):
    '''
    Demonstra o extrato da conta informada
    '''
    print(f"número: {conta['numero']}\nsaldo: {conta['saldo']}")

