from collections import MutableSequence
from conta import Conta

class Contas(MutableSequence):

    _dados = []

    def __len__(self):
        return len(self._dados)
    
    def __getitem__(self, posicao):
        return self._dados[posicao]

    def __setitem__(self, posicao, valor):
        if isinstance(valor, Conta):
            self._dados[posicao] = valor
        else:
            raise TypeError("Valor atribuído não é uma conta")
    
    def __delitem__(self, posicao):
        del self._dados[posicao]

    def insert(self, posicao, valor):
        if isinstance(valor, Conta):
            return self._dados.insert(posicao, valor)
        else:
            raise TypeError("Valor atribuído não é uma conta")
        

    


if __name__ == '__main__':
    import csv
    from conta import ContaCorrente
    from data import Data

    data = Data(16, 12, 2019)

    contas = Contas()
    arquivo = open('contas.txt', 'r')
    leitor = csv.reader(arquivo)

    for linha in leitor:
        conta = ContaCorrente(linha[0], linha[1], float(linha[2]), float(linha[3]), data)
        conta.atualiza(0.0123)
        contas.append(conta)

    arquivo.close()

    print('Saldo\t\tImposto')
    print('-----\t\t-------')
    for c in contas:
        print(f'{c.saldo}\t\t{c.get_valor_imposto()}')
