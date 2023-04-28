import re
class Token:
    def __init__(self,tipo,valor,linha) -> None:
        self.tipo: tipo
        self.valor: valor
        self.linha: linha