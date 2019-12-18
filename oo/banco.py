class Banco:

    def __init__(self):
        self._contas = []
    
    
    def adiciona_conta(self, conta):
        self._contas.append(conta)
    
    def pega_conta(self, id):
        for c in self._contas:
            if c.id == id:
                return c
    
    def pega_total_contas(self):
        return len(self._contas)


if __name__ == '__main__':
    from data import Data
    from atualizador_contas import AtualizadorDeContas
    from conta import Conta, ContaCorrente, ContaPoupanca

    data = Data(17, 12, 2019)

    # Abertura das contas
    c = Conta('123-4', 'João', 1000.0, 5000.0, data)
    cc = ContaCorrente('123-5', 'José', 1000.0, 5000.0, data)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0, 5000.0, data)

    lista_ids = []
    lista_ids.append(c.id)
    lista_ids.append(cc.id)
    lista_ids.append(cp.id)

    banco = Banco()
    banco.adiciona_conta(c)
    banco.adiciona_conta(cc)
    banco.adiciona_conta(cp)

    adc = AtualizadorDeContas(0.01)
    
    for id in lista_ids:
        adc.roda(banco.pega_conta(id))

    print(f'Saldo total: {adc.saldo_total}')