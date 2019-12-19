class Banco:

    def __init__(self):
        self._contas = []
    
    
    def adiciona_conta(self, conta):
        self._contas.append(conta)
    
    def pega_conta(self, numero):
        for c in self._contas:
            if c.numero == numero:
                return c
        return None
    
    def pega_total_contas(self):
        return len(self._contas)


if __name__ == '__main__':
    from data import Data
    from atualizador_contas import AtualizadorDeContas
    from conta import Conta, ContaCorrente, ContaPoupanca, ContaInvestimento
    from cliente import Cliente

    data = Data(17, 12, 2019)

    # Cadastro Clientes:
    joao = Cliente('João', 'da Silva', '333444555-66')
    bicca = Cliente('Bruno', 'Bicca', '111222333-44')
    marcelo = Cliente('Marcelo', 'Frasca', '222333444-55')

    # Abertura das contas
    c = ContaInvestimento('123-4', joao, 1000.0, 5000.0, data)
    cc = ContaCorrente('123-5', bicca, 1000.0, 5000.0, data)
    cp = ContaPoupanca('123-6', marcelo, 1000.0, 5000.0, data)

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