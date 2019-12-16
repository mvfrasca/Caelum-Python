from historico import Historico

class Conta:

    def __init__(self, numero, titular, saldo, limite, data_abertura):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.data_abertura  = data_abertura
        self.historico = Historico()
    
    def deposita(self, valor):
        '''
        Realiza um depósito acrescentando o valor informado ao saldo da conta
        '''
        self.saldo += valor
        self.historico.atualiza_historico(f'Depósito realizado no valor de {valor}')

    def saca(self, valor):
        '''
        Realiza um saque deduzindo o valor informado do saldo da conta
        '''
        if (self.saldo < valor):
            return False
        else:
            self.saldo -= valor
            self.historico.atualiza_historico(f'Saque realizado no valor de {valor}')
            return True
    
    def transfere_para(self, destino, valor):
        '''
        Realiza uma transferência do valor informado para a conta destino
        '''
        retirou = self.saca(valor)
        if (retirou == False):
            return False
        else:
            destino.deposita(valor)
            self.historico.atualiza_historico(f'Transferência realizada no valor de {valor} para a conta número {destino.numero} - titular: {destino.titular.nome} {destino.titular.sobrenome}')
            return True

    def extrato(self):
        '''
        Demonstra o extrato da conta informada
        '''
        print(f"Titular: {self.titular.nome} {self.titular.sobrenome}\nCPF: {self.titular.cpf}") 
        print(f"Conta número: {self.numero}\nSaldo: {self.saldo}")
        print('\n')
        self.historico.imprime()
    