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
        self._historico.atualiza_historico(f'Depósito realizado no valor de {valor}. Saldo parcial: {self._saldo}')

    def saca(self, valor):
        '''
        Realiza um saque deduzindo o valor informado do saldo da conta
        '''
        if (self._saldo < valor):
            return False
        else:
            self._saldo -= valor
            self._historico.atualiza_historico(f'Saque realizado no valor de {valor}. Saldo parcial: {self._saldo}')
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
            self._historico.atualiza_historico(f'Transferência realizada no valor de {valor} para a conta número {destino.numero} - titular: {destino.titular.nome} {destino.titular.sobrenome}. Saldo parcial: {self._saldo}')
            return True

    def extrato(self):
        '''
        Demonstra o extrato da conta informada
        '''
        print(f"Titular: {self._titular.nome} {self._titular.sobrenome}\nCPF: {self._titular.cpf}") 
        print(f"Conta número: {self._numero}\nSaldo: {self._saldo}")
        print('\n')
        self._historico.imprime()


    def atualiza(self, taxa):
        '''
        Atualiza o saldo com a taxa informada
        '''
        self._saldo += self._saldo * taxa
        self._historico.atualiza_historico(f'Atualização de rendimentos - taxa: {taxa}. Saldo parcial: {self._saldo}')
    
    def __str__(self):
        return f"Titular: {self._titular.nome} {self._titular.sobrenome} - CPF: {self._titular.cpf}"

class ContaCorrente(Conta):

    def atualiza(self, taxa):
        '''
        Atualiza o saldo com a taxa informada
        '''
        self._saldo += self._saldo * taxa * 2
        self._historico.atualiza_historico(f'Atualização de rendimentos - taxa: {taxa}. Saldo parcial: {self._saldo}')

    def deposita(self, valor):
        '''
        Realiza um depósito acrescentando o valor informado ao saldo da conta
        '''
        taxa_deposito = 0.1
        self._saldo += valor
        self._historico.atualiza_historico(f'Depósito realizado no valor de {valor}')
        self._saldo -= taxa_deposito
        self._historico.atualiza_historico(f'Cobrança da taxa de depósito {-taxa_deposito}')
        

class ContaPoupanca(Conta):

    def atualiza(self, taxa):
        '''
        Atualiza o saldo com a taxa informada
        '''
        self._saldo += self._saldo * taxa * 3
        self._historico.atualiza_historico(f'Atualização de rendimentos - taxa: {taxa}. Saldo parcial: {self._saldo}')

    

# Testes
if __name__ == "__main__":

    from cliente import Cliente
    from conta import Conta
    from data import Data

    data = Data(16, 12, 2019)

    # Cadastro Clientes:
    joao = Cliente('João', 'da Silva', '333444555-66')
    bicca = Cliente('Bruno', 'Bicca', '111222333-44')
    marcelo = Cliente('Marcelo', 'Frasca', '222333444-55')

    # Abertura das contas:
    conta_joao = Conta('8901-2', joao, 1400.0, 2000.0, data)
    conta_bicca = ContaCorrente('1234-5', bicca, 15000.0, 30000.0, data)
    conta_marcelo = ContaPoupanca('4567-5', marcelo, 5000.0, 10000.0, data)

    #print('Métodos da class Conta:')
    #vars(conta_marcelo)

    # Movimentações nas contas
    conta_joao.saca(100.0)
    conta_bicca.deposita(50.0)
    conta_marcelo.saca(50.0)
    conta_bicca.transfere_para(conta_marcelo, 100.50)
    conta_marcelo.deposita(0.5)
    conta_marcelo.saca(101.0)
    conta_joao.transfere_para(conta_bicca, 350.50)

    # Atualização de rendimentos
    conta_joao.atualiza(0.01)
    conta_bicca.atualiza(0.01)
    conta_marcelo.atualiza(0.01)

    # Extrato
    print(f'\nTotal de Contas: {Conta.total_contas()}')
    print(f'\nConta do João - Id: {conta_joao.id}')
    conta_joao.extrato()
    print(f'\nConta do Bicca - Id: {conta_bicca.id}')
    conta_bicca.extrato()
    print(f'\nConta do Marcelo - Id: {conta_marcelo.id}')
    conta_marcelo.extrato()

    # Impressão dos dados da conta
    print('')
    print(conta_joao)
    print(conta_bicca)
    print(conta_marcelo)