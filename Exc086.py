# dado=list()
# matrix=list()
# for c in range (1,10):
#     print(f'Digite um numero para a posição {c}')
#     dado.append(int(input('')))
#     matrix.append(dado[:])
#     dado.clear
# print('=-'*30)
# print(f' [ {dado[0]} ] [ {dado[1]} ] [ {dado[2]} ]\n [ {dado[3]} ] [ {dado[4]} ] [ {dado[5]} ]\n [ {dado[6]} ] [ {dado[7]} ] [ {dado[8]} ]')



# Lista de Listas - Famosa MATRIZ (matrix em ingles)
[2,3,3,4,4,5,4,6,5,67,75] # lista cabe varios elementos

[[],[],[],[],[],[]] # mas, em cada posição vc pode ter qualquer elemento, como, outra lista por exemplo

# Sabendo que uma MATRIZ é uma estrutura de LINHAS e COLUNAS (como uma tabela)
#            coluna 1  |  coluna 2  |  coluna 3
# linha 1 |     1      |     2      |     3
# linha 2 |     4      |     5      |     6
# linha 3 |     7      |     8      |     9

# Para armazenar uma matriz usando as listas em python, voce pode imaginar que
# - Cada posição da lista "mãe" é uma LINHA da sua matriz
# - cada LINHA possui dentro uma outra lista  "filha" onde cada posição é uma COLUNA
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

matrix[2][1]

# como iterar sobre uma matriz?
# com DOIS fors
# - Um para iterar sobra cada LINHA
# - E outro INTERNO para iterar sobre cada COLUNA da linha atual
N_LINHAS = 3
N_COLUNAS = 3

matrix_top = list() # inicio uma lista vazia

for linha in range(0, N_LINHAS):
    matrix_top.append(list()) # PARA CADA "LINHA" (cada iteração do for de cima), crio uma lista vazia para ser a linha
    for coluna in range(0, N_COLUNAS): # PARA CADA "COLUNA" da LINHA, dou append do dado do usuário
        matrix_top[linha].append(int(input('Digite o número da posção ' + str(linha) + 'x' + str(coluna) + ' da matriz: ')))

print(matrix_top)
