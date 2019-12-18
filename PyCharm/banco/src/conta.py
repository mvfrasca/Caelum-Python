class Conta(object):
    
    def __init__(self, numero, titular, saldo, limite):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

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
        return self._titular

    @limite.setter
    def limite(self, valor):
        self._limite = valor
        return True

    def deposita(self, valor):
        self._saldo += valor

    def saca(self, valor):
        if self._saldo < valor:
            return False
        else:
            self._saldo -= valor
            return True

    def transfere_para(self, conta_destino, valor):
        if self.saca(valor):
            conta_destino.deposita(valor)
            return True
        else:
            return False

    def extrato(self):
        print(f"Titular: {self._titular.nome} {self._titular.sobrenome} -  CPF: {self._titular.cpf}")
        print(f"Conta número: {self._numero}\nSaldo: {self._saldo}")
        print('\n')


if __name__ == '__main__':
    
    from cliente import Cliente

    # Cadastro dos clientes
    joao = Cliente('João', 'da Silva', '111222333-44')
    bicca = Cliente('Bruno', 'Bicca', '222333444-44')
    marcelo = Cliente('Marcelo', 'Frasca', '333444555-44')

    # Abertura das contas
    conta_joao = Conta('123-4', joao, 1200.0, 1000.0)
    conta_bicca = Conta('234-5', bicca, 500.0, 1000.0)
    conta_marcelo = Conta('456-7', marcelo, 200.0, 1000.0)

    # Movimentações
    conta_joao.deposita(200.0)
    conta_bicca.saca(200.55)
    conta_bicca.transfere_para(conta_marcelo, 150.2)
    conta_joao.transfere_para(conta_bicca, 50.0)
    conta_marcelo.saca(150.0)

    #Extrato
    conta_joao.extrato()
    conta_bicca.extrato()
    conta_marcelo.extrato()