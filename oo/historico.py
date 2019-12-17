class Historico:

    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def atualiza_historico(self,texto_historico):
        self._transacoes.append(texto_historico)

    def imprime(self):
        '''
        Imprime o histórico de transações da conta.
        '''
        print('Histórico de Transações')
        print('-----------------------')
        for t in self._transacoes:
            print(f' - {t}')