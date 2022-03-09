linha=3
coluna=3
matrix=list()
par=0
for linhas in range(0,linha):
     matrix.append(list())
     for colunas in range(0,coluna):
          matrix[linhas].append(int(input(f'Digite o número da posção  {linhas} x {colunas}  da matrix: ')))
          if matrix % 2 == 0:
               par += matrix
print(matrix[0])
print(matrix[1])
print(matrix[2])

colu3=matrix[0][2] + matrix[1][2] + matrix[2][2]
print(f'A soma dos valores pares é {par}')
print(f'A soma da coluna 3 é {colu3}')
print(f'O maior valor da segunda linha é {max(matrix[1])}')



#dado=list()
#matrix=list()
#for c in range (1,10):
#     print(f'Digite um numero para a posição {c}')
#     dado.append(int(input('')))
#     matrix.append(dado[:])
#     dado.clear
#print('=-'*30)
#print(f' [ {dado[0]} ] [ {dado[1]} ] [ {dado[2]} ]\n [ {dado[3]} ] [ {dado[4]} ] [ {dado[5]} ]\n [ {dado[6]} ] [ {dado[7]} ] [ {dado[8]} ]')

