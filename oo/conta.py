from historico import Historico

class Conta:
    '''
    Representação de uma Conta bancária.

    Atributos:
    numero: número da conta
    titular: objeto do tipo Cliente representando o titular da conta
    saldo: saldo inicial da conta
    limite: limite de cheque especial da conta
    data_abertura: objeto do tipo Data representando a data de abertura da conta
    '''

    # definir os Slots impede que se crie novos atributos na classe dinamicamente em tempo 
    # de execução (ele apaga o __dict__) 
    __slots__ = ['_id', '_numero', '_titular', '_saldo', '_limite', '_data_abertura', '_historico']
    _total_contas = 0

    def __init__(self, numero, titular, saldo, limite, data_abertura):
        Conta._total_contas += 1
        self._id = Conta._total_contas
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._data_abertura  = data_abertura
        self._historico = Historico()

    @property
    def id(self):
        return self._id   

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        self._titular = valor

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        self._limite = valor
    
    @property
    def data_abertura(self):
        return self._data_abertura

    @data_abertura.setter
    def data_abertura(self, valor):
        self._data_abertura = valor

    @property
    def historico(self):
        return self._historico

    
    @classmethod
    def total_contas(cls):
        return cls._total_contas


    def deposita(self, valor):
        '''
        Realiza um depósito acrescentando o valor informado ao saldo da conta
        '''
        self._saldo += valor
        self._historico.atualiza_historico(f'Depósito realizado no valor de {valor}')

    def saca(self, valor):
        '''
        Realiza um saque deduzindo o valor informado do saldo da conta
        '''
        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self._historico.atualiza_historico(f'Saque realizado no valor de {valor}')
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
            self._historico.atualiza_historico(f'Transferência realizada no valor de {valor} para a conta número {destino.numero} - titular: {destino.titular.nome} {destino.titular.sobrenome}')
            return True

    def extrato(self):
        '''
        Demonstra o extrato da conta informada
        '''
        print(f"Titular: {self._titular.nome} {self._titular.sobrenome}\nCPF: {self._titular.cpf}") 
        print(f"Conta número: {self._numero}\nSaldo: {self._saldo}")
        print('\n')
        self._historico.imprime()
    

    # Testes
    if __name__ == "__main__":

        from cliente import Cliente
        from conta import Conta
        from data import Data

        data = Data(16, 12, 2019)
        bicca = Cliente('Bruno', 'Bicca', '111222333-44')
        marcelo = Cliente('Marcelo', 'Frasca', '222333444-55')

        conta_bicca = Conta('1234-5', bicca, 15000.0, 30000.0, data)
        conta_marcelo = Conta('1234-5', marcelo, 5000.0, 10000.0, data)

        #print('Métodos da class Conta:')
        #vars(conta_marcelo)

        # Movimentações nas contas
        conta_bicca.deposita(50.0)
        conta_marcelo.saca(50.0)
        conta_bicca.transfere_para(conta_marcelo, 100.50)
        conta_marcelo.deposita(0.5)
        conta_marcelo.saca(101.0)

        print(f'\nTotal de Contas: {Conta.total_contas()}')
        print(f'\nConta do Bicca - Id: {conta_bicca.id}')
        conta_bicca.extrato()
        print(f'\nConta do Marcelo - Id: {conta_marcelo.id}')
        conta_marcelo.extrato()

