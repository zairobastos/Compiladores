from lexico import Lexico
from token_1 import Token

nome_arquivo = './data/codigo.txt'
analisador_lexico = Lexico(nome_arquivo)
tokens = analisador_lexico.analisador()

# Escreve os tokens em um arquivo de saída
c=0
with open("./data/tokens.txt", "w") as arquivo:
    for tipo, valor, linha in tokens:
        arquivo.write(f"{tipo}: {valor} (linha {linha})\n")
        c+=1