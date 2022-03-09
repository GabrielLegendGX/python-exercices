fibona=int(input('Quantos termos da sequencia de fibonacci você quer mostrar? '))
n1=0
n2=1
cont=3
while cont <=fibona:
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    cont+=1
