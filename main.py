from lexico import Lexico
from sintatico import Sintatico
from token_1 import Token

nome_arquivo = './data/codigo.txt'
analisador_lexico = Lexico(nome_arquivo)
tokens = analisador_lexico.analisador()

analise_sint = True

# Escreve os tokens em um arquivo de saída
c=0
with open("./data/tokens.txt", "w") as arquivo:
    for tipo, valor, linha in tokens:
        arquivo.write(f"{tipo}: {valor} (linha {linha})\n")
        c+=1
        if(tipo == 'ERROR'):
            print("Erro na análise léxica: o caractere '{}' é inesperado na linha {}".format(valor, linha))
            analise_sint = False
            break


if(analise_sint):
    analisador_sintatico = Sintatico(tokens)
    # Inicia a análise sintática
    analisador_sintatico.programa()

    if(analisador_sintatico.erros.count == 0):
        print("Análise sintática sem erros concluída com sucesso.")
    else:
        for erros in analisador_sintatico.erros:
            print(erros)
