from conta import Conta, ContaCorrente, ContaPoupanca

class AtualizadorDeContas():

    def __init__(self, taxa, saldo_total=0.0):
        self._taxa = taxa
        self._saldo_total = saldo_total

    @property
    def taxa(self):
        return self._taxa
    
    @taxa.setter
    def taxa(self, valor):
        self.taxa = valor

    @property
    def saldo_total(self):
        return self._saldo_total

    def roda(self, conta):
        '''
        Imprime o saldo anterior, atualiza a conta e depois imprime o saldo final
        Soma o saldo final ao atributo saldo_total
        '''
        print(f'Saldo anterior: {conta.saldo}')
        conta.atualiza(self._taxa)
        print(f'Saldo final: {conta.saldo}')
        self._saldo_total += conta.saldo

if __name__ == '__main__':
    from data import Data
    data = Data(17, 12, 2019)

    # Abertura das contas
    c = Conta('123-4', 'João', 1000.0, 5000.0, data)
    cc = ContaCorrente('123-5', 'José', 1000.0, 5000.0, data)
    cp = ContaPoupanca('123-6', 'Maria', 1000.0, 5000.0, data)

    adc = AtualizadorDeContas(0.01)

    adc.roda(c)
    adc.roda(cc)
    adc.roda(cp)

    print(f'Saldo total: {adc.saldo_total}')