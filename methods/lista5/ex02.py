'''2. Faça um programa contendo uma função/método que mostre uma matriz. Na passagem de parâmetro use a matriz apenas. A quantidade de linhas e colunas, dentro da funcão identifique, usando o comando len.'''

# def matriz(l, c):
#     matriz = []
#     for lin in range(l):
#         linha = []
#         for col in range(c):
#             linha.append(int(input("Digite o valor de ['{},{}']: ".format(lin, col))))
#         matriz.append(linha)
#     return matriz

# def qtd_l_c(m):
#     for i in range(len(m)):
#         len(m[i])
#         len(m)
#         return print('A matriz tem {} linhas e {} colunas.'.format(len(m), len(m[i])))

# def main():
#     n_linhas = int(input('Digite o número linhas a ser inserida -> '))
#     n_col = int(input('Digite o número colunas a ser inserida -> '))
#     aux = matriz(n_linhas, n_col)
#     print(aux)
#     qtd_l_c(aux)
    
# main()

def matriz(l, c):
    matriz = []
    for lin in range(l):
        linha = []
        for col in range(c):
            linha.append(int(input("Digite o valor de ['{},{}']: ".format(lin, col))))
        matriz.append(linha)
    return matriz

def qtd_l_c(m):
    for lin in range(len(m)): # lin percorre o tamanho das linhas da matriz (m)
        for col in range(len(m[lin])): # col percorre o tamanho das colunas/ vetores dentro de cada linha
            print(m[lin][col], end='\t') # imprime o resultado formatado
        print()

def main():
    n_linhas = int(input('Digite o número linhas a ser inserida -> '))
    n_col = int(input('Digite o número colunas a ser inserida -> '))
    # print(matriz(n_linhas, n_col))
    qtd_l_c(matriz(n_linhas, n_col))

main()