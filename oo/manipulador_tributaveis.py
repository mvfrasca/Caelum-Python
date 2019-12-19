from tributavel import Tributavel

class ManipuladorDeTributaveis:

    def calcula_impostos(self, lista_tributaveis):
        total = 0.0
        for t in lista_tributaveis:
            if(isinstance(t, Tributavel)):
                total += t.get_valor_imposto()
            else:
                print(f'{t.__repr__()} não é tributável. Produto bancário: {t}')
        return total

if __name__ == '__main__':

    from cliente import Cliente
    from conta import Conta, ContaCorrente, ContaPoupanca, ContaInvestimento, SeguroDeVida
    from data import Data

    data = Data(16, 12, 2019)

    # Cadastro Clientes:
    joao = Cliente('João', 'da Silva', '333444555-66')
    bicca = Cliente('Bruno', 'Bicca', '111222333-44')
    marcelo = Cliente('Marcelo', 'Frasca', '222333444-55')

    # Abertura das contas:
    conta_joao = ContaInvestimento('8901-2', joao, 1400.0, 2000.0, data)
    conta_bicca = ContaCorrente('1234-5', bicca, 15000.0, 30000.0, data)
    conta_marcelo = ContaPoupanca('4567-5', marcelo, 5000.0, 10000.0, data)
    seguro_marcelo = SeguroDeVida(50000.0, marcelo, '123456')
    
    # Registrando a interface Tributavel nos objetos que se pretende atribuir o mesmo comportamento
    Tributavel.register(ContaCorrente)
    Tributavel.register(ContaInvestimento)
    Tributavel.register(SeguroDeVida)
    
    lista_tributaveis = []
    lista_tributaveis.append(conta_joao)
    lista_tributaveis.append(conta_bicca)
    lista_tributaveis.append(conta_marcelo)
    lista_tributaveis.append(seguro_marcelo)

    print('')
    for t in lista_tributaveis:
        print(t)
        if(isinstance(t, Tributavel)):
            print(f'Valor imposto: {t.get_valor_imposto()}')
        else:
            print(f'{t.__repr__()} não é tributável')

    print('')
    mt = ManipuladorDeTributaveis()
    total = mt.calcula_impostos(lista_tributaveis)
    print(f'Total Imposto: {total}')