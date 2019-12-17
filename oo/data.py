class Data:

    def __init__(self, dia, mes, ano):
        self._dia = dia
        self._mes = mes
        self._ano = ano
    
    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, valor):
        self._dia = valor
    
    @property
    def mes(self):
        return self._mes

    @mes.setter
    def mes(self, valor):
        self._mes = valor

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, valor):
        self._ano = valor