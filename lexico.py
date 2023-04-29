import re
class Lexico:
    def __init__(self, arquivo):
        with open(arquivo,'r') as arq:
            self.codigo = arq.read()
    
    # Define as expressões regulares para cada tipo de token
    regexs = {
        'COMENTÁRIO': r'#[^#]*#',
        'TIPO DE DADO': r'int[\[\]]*|decimal[\[\]]*|bool[\[\]]*|char[\[\]]*',
        'PALAVRA RESERVADA': r'static|void|Main|if|args|string\[\]',
        'IDENTIFICADOR': r'[a-z_][a-zA-Z0-9_]*',
        'NUMERO DECIMAL': r'\d+.\d+',
        'NUMERO INTEIRO': r'\d+',
        'BOOLEANO': r'True|False',
        'OPERADOR ARITMÉTICO': r'[+\-*/%]',
        'SÍMBOLO DE COMPARAÇÃO': r'==|!=',
        'OPERADOR LÓGICO': r'\|\||&&|!',
        'OPERADOR RELACIONAL': r'>=|>|<=|<',
        'ATRIBUIÇÃO': r'=',
        'SÍMBOLOS': r'[{}():]',
        'ESPAÇO EM BRANCO': r'\s',
        'QUEBRA DE LINHA': r'\n',
    }
    
    def analisador(self):
        tokens = []
        linha = 1
        posicao = 0

        while posicao < len(self.codigo):
            match = None
            for tipo, regex in self.regexs.items():
                match = re.match(regex, self.codigo[posicao:])
                if match:
                    if tipo != 'ESPAÇO EM BRANCO' and tipo != 'QUEBRA DE LINHA':
                        valor = match.group()
                        tokens.append((tipo, valor, linha))
                        posicao += len(valor)
                    elif tipo == 'QUEBRA DE LINHA':
                        linha += 1
                        posicao += 1
                    else:
                        posicao += 1
                    break
            else:
                tokens.append(('ERROR', self.codigo[posicao], linha))
                posicao += 1

            if posicao < len(self.codigo) and self.codigo[posicao] == '\n':
                linha += 1
                posicao += 1

        return tokens
