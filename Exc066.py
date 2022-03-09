n=0
s=0
cont=0
while True:
    n=int(input('Digite um numero '))
    cont+=1
    s+=n
    if n==999:
        break
print(f'a soma entre esses numeros foi {s-999} e foi digitado {cont-1} numeros')