class Cliente:

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, valor):
        self._sobrenome = valor

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        self._cpf = valor

