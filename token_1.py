import re
class Token:
    def __init__(self,tipo,valor,linha):
        self.tipo: tipo
        self.valor: valor
        self.linha: linha