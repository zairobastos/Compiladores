from token_1 import Token

class Sintatico:

    def __init__(self, tokens):
        self.tokens = tokens
        self.indice = 0
        self.linha_atual = 0
        self.token_atual = None

    def proximo_token(self):
        if self.indice < len(self.tokens):
            self.token_atual = self.tokens[self.indice]
            self.indice += 1
        else:
            self.token_atual = None

    def erro(self, esperado):
        if self.token_atual is None:
            mensagem = f"Fim do código. Esperado: {esperado}"
        else:
            mensagem = f"Erro na linha {self.token_atual[2]}. Esperado: {esperado}. Encontrado: {self.token_atual[0]} \"{self.token_atual[1]}\""
 
        raise Exception(mensagem)
    
    def erro_linha(self, esperado, next_line):
        if(next_line):
            raise Exception(f"Fim da linha {self.token_atual[2] - 1}. Esperado: {esperado}")
        
        raise Exception(f"É esperado uma quebra de linha antes de {esperado}")

    def programa(self):
        
        self.proximo_token()
        linha_codigo = self.token_atual[2]
        if self.token_atual[0] != 'PALAVRA RESERVADA' or self.token_atual[1] != 'static':
            self.erro('Palavra reservada "static"')

        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('Palavra reservada "void"', 1)

        if self.token_atual[0] != 'PALAVRA RESERVADA' or self.token_atual[1] != 'void':
            self.erro('Palavra reservada "void"')

        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('Palavra reservada "Main"', 1) 
            
        if self.token_atual[0] != 'PALAVRA RESERVADA' or self.token_atual[1] != 'Main':
            self.erro('Palavra reservada "Main"')

        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('Simbolo "("', 1) 
        if self.token_atual[0] != 'SÍMBOLOS' or self.token_atual[1] != '(':
            self.erro('Simbolo "("')

        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('Palavra reservada "string[]"', 1) 
        if self.token_atual[0] != 'PALAVRA RESERVADA' or self.token_atual[1] != 'string[]':
            self.erro('Palavra reservada "string[]"')

        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('Palavra reservada "args"', 1) 
        if self.token_atual[0] != 'PALAVRA RESERVADA' or self.token_atual[1] != 'args':
            self.erro('Palavra reservada "args"')  

        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('Simbolo ")"', 1)    
        if self.token_atual[0] != 'SÍMBOLOS' or self.token_atual[1] != ')':
            self.erro('Simbolo ")"')
            

        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('Simbolo ":"', 1)  

        if self.token_atual[0] != 'SÍMBOLOS' or self.token_atual[1] != ':':
            self.erro('Simbolo ":"')   

        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.declaracoes()
        else:
            self.erro_linha(f'{self.token_atual[0]} {self.token_atual[1]} na linha {self.token_atual[2]}', 0)
        
        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.comandos()
        else:
            self.erro_linha(f'{self.token_atual[0]} {self.token_atual[1]} na linha {self.token_atual[2]}', 0)
    
    def declaracoes(self):
        
        if self.token_atual[0] != 'TIPO DE DADO' and self.token_atual[0] != 'CONSTANTE':
            self.erro('TIPO DE DADO OU "CONST"')
        else:
            while self.token_atual[0] == 'TIPO DE DADO' or self.token_atual[0] == 'CONSTANTE':
                if self.token_atual[0] == 'TIPO DE DADO':
                    self.declaracao()
                elif self.token_atual[0] == 'CONSTANTE':
                    self.declaracao_const()

    def declaracao(self): 
        linha_codigo = self.token_atual[2]

        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('IDENTIFICADOR', 1) 
        if self.token_atual[0] != 'IDENTIFICADOR':
            self.erro('IDENTIFICADOR')

        self.proximo_token()
        if(linha_codigo == self.token_atual[2]):
            if (self.token_atual[0] == 'SÍMBOLOS' and self.token_atual[1] == '['):
                self.proximo_token()
                if(linha_codigo != self.token_atual[2]):
                    self.erro_linha('NUMERO INTEIRO', 1) 
                
                if self.token_atual[0] != 'NUMERO INTEIRO':
                    self.erro('NUMERO INTEIRO')
                else:
                    self.proximo_token()
                    if(linha_codigo != self.token_atual[2]):
                        self.erro_linha('Simbolo "]"', 1) 

                    if self.token_atual[0] != 'SÍMBOLOS' or self.token_atual[1] != ']':
                        self.erro('Simbolo "]"')

                    self.proximo_token()
                    if(linha_codigo == self.token_atual[2]): 
                        if (self.token_atual[0] == 'SÍMBOLOS' and self.token_atual[1] == ','):
                            self.declaracao()
                        else:
                            self.erro('Simbolo ","')
                    else:
                        self.erro_linha('Simbolo ","', 1)

            elif (self.token_atual[0] == 'SÍMBOLOS' and self.token_atual[1] == ','):
                self.declaracao()
            else:
                self.erro('SIMBOLO "[" OU ","')
        else:
            self.declaracoes()

    def declaracao_const(self):
        linha_codigo = self.token_atual[2]
        
        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('IDENTIFICADOR', 1) 
        if self.token_atual[0] != 'IDENTIFICADOR':
            self.erro('IDENTIFICADOR')

        self.proximo_token()    
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('NUMERO DECIMAL OU INTEIRO', 1)
        if self.token_atual[0] != 'NUMERO DECIMAL' and self.token_atual[0] != 'NUMERO INTEIRO':
            self.erro('NUMERO DECIMAL OU INTEIRO')
    
    def comandos(self):

        if self.token_atual[0] != 'IDENTIFICADOR' and self.token_atual[1] != 'if':
            self.erro('IDENTIFICADOR OU PALAVRA RESERVADA "if"')
        else:
            while self.token_atual[0] == 'IDENTIFICADOR' or (self.token_atual[0] == 'PALAVRA RESERVADA' and self.token_atual[1] == 'if'):
                self.comando()

    def comando(self):
        if self.token_atual[0] == 'IDENTIFICADOR':
            self.atribuicao()
        elif self.token_atual[0] == 'PALAVRA RESERVADA' and self.token_atual[1] == 'if':
            self.condicional()
        else:
            self.erro('IDENTIFICADOR OU PALAVRA RESERVADA "if"')

    def atribuicao(self):
        self.consumir_token(Token.IDENTIFICADOR)
        self.consumir_token(Token.ATRIBUIÇÃO)
        if self.proximo_token() and self.proximo_token().tipo == Token.IDENTIFICADOR:
            self.expressao_simples()
        else:
            self.expressao()

    def condicional(self):
        self.consumir_token(Token.PALAVRA_RESERVADA, "if")
        self.consumir_token(Token.SÍMBOLOS, "(")
        self.expressao()
        if self.proximo_token() and self.proximo_token().tipo == Token.SÍMBOLOS and self.proximo_token().valor in ("==", "!="):
            self.consumir_token(Token.SÍMBOLOS)
            self.expressao()
        self.consumir_token(Token.SÍMBOLOS, ")")
        self.consumir_token(Token.SÍMBOLOS, "{")
        self.declaracoes()
        self.comandos()
        self.consumir_token(Token.SÍMBOLOS, "}")
        if self.proximo_token() and self.proximo_token().tipo == Token.PALAVRA_RESERVADA and self.proximo_token().valor == "else":
            self.consumir_token(Token.PALAVRA_RESERVADA, "else")
            self.consumir_token(Token.SÍMBOLOS, "{")
            self.declaracoes()
            self.comandos()
            self.consumir_token(Token.SÍMBOLOS, "}")

    def expressao(self):
        linha_codigo = self.token_atual[2]

        self.proximo_token()
        if(linha_codigo != self.token_atual[2]):
            self.erro_linha('OPERADOR LÓGICO "!", IDENTIFICADOR OU VALOR DE VARIAVEL', 1)
        
        if self.token_atual[0] == 'OPERADOR LÓGICO' and self.token_atual[1] == '!': #NEGAÇÃO
            self.negacao()

        # EXPRESSÕES (LÓGICA OU ARITMETICA)
        elif self.token_atual[0] == 'IDENTIFICADOR' or self.token_atual[0] == 'NUMERO INTEIRO' or self.token_atual[0] == 'NUMERO DECIMAL' or self.token_atual[0] == 'BOOLEANO' or self.token_atual[0] == 'STRING':
            self.proximo_token()

            if(linha_codigo != self.token_atual[2]):
                self.erro_linha('OPERADOR LÓGICO OU ARITMÉTICO', 1)

            if self.token_atual[0] == 'OPERADOR LÓGICO':
                self.expressao_logica()
            elif self.token_atual[0] == 'OPERADOR ARITMÉTICO':
                self.expressao_arit()
            else:
                self.erro('OPERADOR LÓGICO OU ARITMÉTICO', 1)
        else:
            self.erro('OPERADOR LÓGICO "!", IDENTIFICADOR, NUMERO INTEIRO, DECIMAL, BOOLEANO OU STRING', 1)

    def negacao(self):
        self.expressao_logica()

    def expressao_logica(self):
        linha_codigo = self.token_atual[2]
        self.proximo_token()

    def expressao_arit(self):
        linha_codigo = self.token_atual[2]

        self.proximo_token()

        if(linha_codigo == self.token_atual[2]):
            self.expressao_simples()
        else:
            self.erro_linha('IDENTIFICADOR, NUMERO INTEIRO, DECIMAL, BOOLEANO OU STRING', 1)

    def expressao_simples(self):

        if self.token_atual[0] != 'IDENTIFICADOR' and self.token_atual[0] != 'NUMERO INTEIRO' and self.token_atual[0] != 'NUMERO DECIMAL' and self.token_atual[0] != 'BOOLEANO' and self.token_atual[0] != 'STRING':
            self.erro('IDENTIFICADOR, NUMERO INTEIRO, DECIMAL, BOOLEANO OU STRING', 1)        