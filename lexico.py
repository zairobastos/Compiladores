import re

# Abre o arquivo com o código fonte
with open("codigo.txt", "r") as arquivo:
    codigo = arquivo.read()

# Define as expressões regulares para cada tipo de token
regex_identificador = r'[a-zA-Z_][a-zA-Z0-9_]*'
regex_numero = r'\d+'
regex_operador = r'[+\-*/%]'
regex_comentario = r'^#[\x00-\x7F]*#$'
regex_palavra_reservada = r'static|void|Main|if|args|string\[\]'
regex_igualdade = r'==|!='
regex_operador_logico = r'\|\||&&|!'
regex_operador_relacional = r'>=|>|<=|<'
regex_atribuicao = r'='
regex_tipo_dado = r'int|decimal|bool|char'

# Define uma lista vazia para armazenar os tokens
tokens = []

# Itera sobre o código fonte e identifica os tokens
posicao = 0
linha = 1
while posicao < len(codigo):
    # Verifica se a posição atual corresponde a um número
    match = re.match(regex_numero, codigo[posicao:])
    if match:
        numero = match.group(0)
        tokens.append(('numero', numero, linha))
        posicao += len(numero)
        continue

    # Verifica se a posição atual corresponde a um operador
    match = re.match(regex_operador, codigo[posicao:])
    if match:
        operador = match.group(0)
        tokens.append(('operador', operador, linha))
        posicao += len(operador)
        continue

    # Verifica se a posição atual corresponde a um comentário
    match = re.match(regex_comentario, codigo[posicao:])
    if match:
        comentario = match.group(0)
        tokens.append(('comentario', comentario, linha))
        posicao += len(comentario)
        continue
    
    # Verifica se a posição atual corresponde a uma palavra reservada
    match = re.match(regex_palavra_reservada, codigo[posicao:])
    if match:
        palavra_reservada = match.group(0)
        tokens.append(('palavra_reservada', palavra_reservada, linha))
        posicao += len(palavra_reservada)
        continue

    # Verifica se a posição atual corresponde a um tipo de dado
    match = re.match(regex_tipo_dado, codigo[posicao:])
    if match:
        tipo_de_dado = match.group(0)
        tokens.append(('tipo_de_dado', tipo_de_dado, linha))
        posicao += len(tipo_de_dado)
        continue
    
    # Verifica se a posição atual corresponde a um identificador
    match = re.match(regex_identificador, codigo[posicao:])
    if match:
        identificador = match.group(0)
        tokens.append(('identificador', identificador, linha))
        posicao += len(identificador)
        continue

    # Verifica se a posição atual corresponde a uma igualdade
    match = re.match(regex_igualdade, codigo[posicao:])
    if match:
        igualdade = match.group(0)
        tokens.append(('igualdade', igualdade, linha))
        posicao += len(igualdade)
        continue
    
    # Verifica se a posição atual corresponde a um operador logico
    match = re.match(regex_operador_logico, codigo[posicao:])
    if match:
        operador_logico = match.group(0)
        tokens.append(('operador_logico', operador_logico, linha))
        posicao += len(operador_logico)
        continue

    # Verifica se a posição atual corresponde a um operador relacional
    match = re.match(regex_operador_relacional, codigo[posicao:])
    if match:
        operador_relacional = match.group(0)
        tokens.append(('operador_relacional', operador_relacional, linha))
        posicao += len(operador_relacional)
        continue

    # Verifica se a posição atual corresponde a uma atribuição
    match = re.match(regex_atribuicao, codigo[posicao:])
    if match:
        operador_de_atribuicao = match.group(0)
        tokens.append(('operador_de_atribuicao', operador_de_atribuicao, linha))
        posicao += len(operador_de_atribuicao)
        continue

    # Verifica se a posição atual corresponde a um caractere de quebra de linha
    if codigo[posicao] == '\n':
        linha += 1

    # Caso contrário, ignora o caractere atual
    posicao += 1

# Escreve os tokens em um arquivo de saída
with open("tokens.txt", "w") as arquivo:
    for tipo, valor, linha in tokens:
        arquivo.write(f"{tipo}: {valor} (linha {linha})\n")