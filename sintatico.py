from lexico import Lexico
from token_1 import Token

class Sintatico:

    def __init__(self, tokens):
        self.tokens = tokens
        self.erros = []  # Lista para armazenar os erros encontrados
        self.indice = 0
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

    def programa(self):
        self.proximo_token()
        if self.token_atual[0] != 'PALAVRA RESERVADA' or self.token_atual[1] != 'static':
            self.erro('Palavra reservada "static"')

        self.proximo_token()
        if self.token_atual[0] != 'PALAVRA RESERVADA' or self.token_atual[1] != 'void':
            self.erro('Palavra reservada "void"')

        self.proximo_token()
        if self.token_atual[0] != 'PALAVRA RESERVADA' or self.token_atual[1] != 'Main':
            self.erro('Palavra reservada "Main"')

        self.proximo_token()
        if self.token_atual[0] != 'SÍMBOLOS' or self.token_atual[1] != '(':
            self.erro('Simbolo "("')
        
        self.proximo_token()
        if self.token_atual[0] != 'PALAVRA RESERVADA' or self.token_atual[1] != 'string[]':
            self.erro('Palavra reservada "string[]"')

        self.proximo_token()
        if self.token_atual[0] != 'PALAVRA RESERVADA' or self.token_atual[1] != 'args':
            self.erro('Palavra reservada "args"')  

        self.proximo_token()
        if self.token_atual[0] != 'SÍMBOLOS' or self.token_atual[1] != ')':
            self.erro('Simbolo ")"')

        self.proximo_token()
        if self.token_atual[0] != 'SÍMBOLOS' or self.token_atual[1] != ':':
            self.erro('Simbolo ":"')

    def analisar(self):
        self.programa()

        self.posicao += 1

    def declaracoes(self):
        while self.proximo_token() and self.proximo_token().tipo == Token.TIPO_DE_DADO:
            self.declaracao()

    def declaracao(self):
        tipo = self.proximo_token().valor
        self.consumir_token(Token.TIPO_DE_DADO)
        self.consumir_token(Token.IDENTIFICADOR)
        if self.proximo_token() and self.proximo_token().tipo == Token.SÍMBOLOS and self.proximo_token().valor == "[":
            self.consumir_token(Token.SÍMBOLOS, "[")
            self.consumir_token(Token.INTEIRO)
            self.consumir_token(Token.SÍMBOLOS, "]")
        while self.proximo_token() and self.proximo_token().tipo == Token.SÍMBOLOS and self.proximo_token().valor == ",":
            self.consumir_token(Token.SÍMBOLOS, ",")
            self.consumir_token(Token.IDENTIFICADOR)
            if self.proximo_token() and self.proximo_token().tipo == Token.SÍMBOLOS and self.proximo_token().valor == "[":
                self.consumir_token(Token.SÍMBOLOS, "[")
                self.consumir_token(Token.INTEIRO)
                self.consumir_token(Token.SÍMBOLOS, "]")

    def comandos(self):
        while self.proximo_token() and self.proximo_token().tipo != Token.COMENTÁRIO:
            self.comando()

    def comando(self):
        if self.proximo_token() and self.proximo_token().tipo == Token.IDENTIFICADOR:
            self.atribuicao()
        elif self.proximo_token() and self.proximo_token().tipo == Token.PALAVRA_RESERVADA and self.proximo_token().valor == "if":
            self.condicional()
        else:
            # Lidar com outros comandos
            pass

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
        if self.proximo_token() and self.proximo_token().tipo == Token.IDENTIFICADOR:
            self.expressao_simples()
        elif self.proximo_token() and self.proximo_token().tipo == Token.PALAVRA_RESERVADA and self.proximo_token().valor == "!":
            self.negacao()
        else:
            # Lidar com outras expressões
            pass

    def negacao(self):
        self.consumir_token(Token.PALAVRA_RESERVADA, "!")
        self.expressao()

    def expressao_simples(self):
        if self.proximo_token() and self.proximo_token().tipo == Token.IDENTIFICADOR:
            self.consumir_token(Token.IDENTIFICADOR)
        elif self.proximo_token() and self.proximo_token().tipo == Token.VARIÁVEL:
            self.consumir_token(Token.VARIÁVEL)
        else:
            # Lidar com outros casos de expressão simples
            pass
