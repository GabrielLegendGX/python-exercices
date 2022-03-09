par=list()
impar=list()
for c in range (1,8):
    print(f'Digite o {c} numero ',end=(' '))
    num=int(input())
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
par.sort(reverse=True)
impar.sort(reverse=True)
print(f'Os numeros pares são {par}')
print(f'Os numeros impares são {impar}')

