from conta import Conta
from banco import Banco
from excecoes import SaldoInsuficienteError, ContaInexistente

class CaixaEletronico:

    def __init__(self, banco, numero_conta):
        self._banco = banco
        conta = banco.pega_conta(numero_conta)
        if conta == None:
            raise ContaInexistente("A conta informada não existe")
        self._conta = conta

    @property
    def conta(self):
        return self._conta

    def deposita(self, valor):
        '''Realiza depósito
        '''
        try:
            self._conta.deposita(valor)
            print("Depósito realizado com sucesso!")
        except ValueError:
            print("O valor informado para depósito deve ser um número positivo.")
        except:
            print("Ocorreu um erro, tente novamente daqui a alguns instantes.")
    
    def saca(self, valor):
        '''Realiza saca
        '''
        try:
            self._conta.saca(valor)
            print("Saque realizado com sucesso!")
        except ValueError:
            print("O valor informado para depósito deve ser um número positivo.")
        except SaldoInsuficienteError:
            print("Você não possui saldo suficiente para completar essa operação.")
        except:
            print("Ocorreu um erro, tente novamente daqui a alguns instantes.")
    
    def transfere_para(self, numero_conta_destino, valor):
        '''Realiza transferência
        '''
        try:
            conta_destino = banco.pega_conta(numero_conta_destino)
            if conta_destino == None:
                raise ContaInexistente("A conta informada não existe")
            else: 
                self._conta.transfere_para(conta_destino, valor)
                print("Transferência realizada com sucesso!")
        except ValueError:
            print("O valor informado para transferência deve ser um número positivo.")
        except SaldoInsuficienteError:
            print("Você não possui saldo suficiente para completar essa operação.")
        except ContaInexistente as e:
            print("A conta informada não existe.")
        except:
            print("Ocorreu um erro, tente novamente daqui a alguns instantes.")

    def extrato(self):
        '''Imprime extrato da conta
        '''
        try:
            self._conta.extrato()
        except:
            print("Ocorreu um erro, tente novamente daqui a alguns instantes.")


if __name__ == '__main__':
    from conta import ContaCorrente, ContaPoupanca, ContaInvestimento
    from cliente import Cliente
    from data import Data

    ## Populando banco ##

    data = Data(16, 12, 2019)

    # Cadastro Clientes:
    joao = Cliente('João', 'da Silva', '333444555-66')
    bicca = Cliente('Bruno', 'Bicca', '111222333-44')
    marcelo = Cliente('Marcelo', 'Frasca', '222333444-55')

    # Abertura das contas
    c = ContaInvestimento('123-4', joao, 1000.0, 5000.0, data)
    cc = ContaCorrente('123-5', bicca, 1000.0, 5000.0, data)
    cp = ContaPoupanca('123-6', marcelo, 1000.0, 5000.0, data)

    banco = Banco()
    banco.adiciona_conta(c)
    banco.adiciona_conta(cc)
    banco.adiciona_conta(cp)


    ## Execução caixa eletrônico ##
    
    numero_conta = input("Informe o número da conta: ")
    caixa_eletronico = CaixaEletronico(banco, numero_conta)

    print(f"Olá Sr(a). {caixa_eletronico.conta.titular.nome}!")

    opcao = 0
    while (opcao != 9):
        print("\nMenu de opções: ")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Transferência")
        print("4 - Extrato")
        print("9 - Sair")
        opcao = int(input("\nInforme a opção desejada: "))

        if opcao == 1:
            valor = float(input("Informe o valor de depósito: "))
            caixa_eletronico.deposita(valor)
        elif opcao == 2:
            valor = float(input("Informe o valor para saque: "))
            caixa_eletronico.saca(valor)
        elif opcao == 3:
            numero_conta_destino = input("Informe o número da conta destino: ")
            valor = float(input("Informe o valor para transferência: "))
            caixa_eletronico.transfere_para(numero_conta_destino, valor)
        elif opcao == 4:
            caixa_eletronico.extrato()