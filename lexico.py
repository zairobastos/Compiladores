import re
class Lexica:
    def __init__(self, arquivo):
        with open(arquivo,'r') as arq:
            self.codigo = arq.read()
    
    # Define as expressões regulares para cada tipo de token
    regexs = {
        'PALAVRA RESERVADA': r'static|void|Main|if|args|string\[\]',
        'COMENTÁRIO': r'^#.*#$',
        'IDENTIFICADOR': r'[a-zA-Z_][a-zA-Z0-9_]*',
        'NUMERO': r'\d+',
        'OPERADOR MATEMÁTICO': r'[+\-*/%]',
        'SÍMBOLO DE COMPARAÇÃO': r'==|!=',
        'OPERADOR LÓGICO': r'\|\||&&|!',
        'OPERADOR RELACIONAL': r'>=|>|<=|<',
        'ATRIBUIÇÃO': r'=',
        'TIPO DE DADO': r'int|decimal|bool|char',
    }
    
    def analisador(self):
        tokens = []
        linha = 1
        posicao = 0

        while posicao < len(self.codigo):
            match = None
            for tipo, regex in self.regexs.items():
                match = re.match(regex,self.codigo[posicao:])
                if match:
                    valor = match.group()
                    tokens.append((tipo,valor,linha))
                    posicao += len(valor)
                    break
            else:
                if self.codigo[posicao] == '\n':
                    linha += 1
                posicao += 1
        return tokens