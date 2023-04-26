import re

# Abre o arquivo com o código fonte
with open("codigo.txt", "r") as arquivo:
    codigo = arquivo.read()

# Define as expressões regulares para cada tipo de token
regex_identificador = r'[a-zA-Z_][a-zA-Z0-9_]*'
regex_numero = r'\d+'
regex_operador = r'[+\-*/%]'

# Define uma lista vazia para armazenar os tokens
tokens = []

# Itera sobre o código fonte e identifica os tokens
posicao = 0
linha = 1
while posicao < len(codigo):
    # Verifica se a posição atual corresponde a um identificador
    match = re.match(regex_identificador, codigo[posicao:])
    if match:
        identificador = match.group(0)
        tokens.append(('identificador', identificador, linha))
        posicao += len(identificador)
        continue

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

    # Verifica se a posição atual corresponde a um caractere de quebra de linha
    if codigo[posicao] == '\n':
        linha += 1

    # Caso contrário, ignora o caractere atual
    posicao += 1

# Escreve os tokens em um arquivo de saída
with open("tokens.txt", "w") as arquivo:
    for tipo, valor, linha in tokens:
        arquivo.write(f"{tipo}: {valor} (linha {linha})\n")