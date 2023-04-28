from lexico import Lexica

nome_arquivo = './data/codigo.txt'
analisador_lexico = Lexica(nome_arquivo)
tokens = analisador_lexico.analisador()

# Escreve os tokens em um arquivo de saída
with open("./data/tokens.txt", "w") as arquivo:
    for tipo, valor, linha in tokens:
        arquivo.write(f"{tipo}: {valor} (linha {linha})\n")