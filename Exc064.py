n=0
cont=0
soma=0
while n != 999:
    n=int(input('Digite um numero[Digite 999 para parar] '))
    cont+=1
    soma+=n
print(('Você digitou {} numeros e a soma entre todos eles é {} ').format(cont -1,soma -999))