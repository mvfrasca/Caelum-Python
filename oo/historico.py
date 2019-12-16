class Historico:

    def __init__(self):
        self.transacoes = []

    def atualiza_historico(self,texto_historico):
        self.transacoes.append(texto_historico)

    def imprime(self):
        '''
        Imprime o histórico de transações da conta.
        '''
        print('Histórico de Transações')
        print('-----------------------')
        for t in self.transacoes:
            print(f' - {t}')