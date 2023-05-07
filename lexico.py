import re
class Lexico:
    def __init__(self, arquivo):
        with open(arquivo,'r') as arq:
            self.codigo = arq.read()
    
    # Define as expressões regulares para cada tipo de token
    regexs = {
        'COMENTÁRIO': r'\/\*[^#]*\*\/',
        'TIPO DE DADO': r'int[\[\]]*|decimal[\[\]]*|bool[\[\]]*|char[\[\]]*',
        'PALAVRA RESERVADA': r'static|void|Main|if|args|string\[\]',
        'IDENTIFICADOR': r'[a-z_][a-zA-Z0-9_]*',
        'NUMERO DECIMAL': r'\d+.\d+',
        'NUMERO DECIMAL DIR': r'\.\d+',
        'NUMERO DECIMAL ESQ': r'\d+\.',
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
            match_regex = None
            for tipo, regex in self.regexs.items():
                match_regex = re.match(regex, self.codigo[posicao:])
                #match match_regex:
                #    case 
                if match_regex:
                    if tipo == 'QUEBRA DE LINHA':
                        linha += 1
                        posicao += 1
                    elif tipo == 'NUMERO DECIMAL DIR':
                        valor = match_regex.group()
                        valor =  "0" + valor
                        tokens.append((tipo, valor, linha))
                        posicao += len(valor)
                    elif tipo == 'NUMERO DECIMAL ESQ':
                        valor = match_regex.group()
                        valor = valor + '0'
                        tokens.append((tipo, valor, linha))
                        posicao += len(valor)
                    elif tipo != 'ESPAÇO EM BRANCO' and tipo != 'COMENTÁRIO':
                        valor = match_regex.group()
                        tokens.append((tipo, valor, linha))
                        posicao += len(valor)
                    else:
                        valor = match_regex.group()
                        posicao += len(valor)
                    break
            else:
                tokens.append(('ERROR', self.codigo[posicao], linha))
                return tokens

            if posicao < len(self.codigo) and self.codigo[posicao] == '\n':
                linha += 1
                posicao += 1

        return tokens
