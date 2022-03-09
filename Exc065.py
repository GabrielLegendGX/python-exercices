escolha='S'
cont=0
soma=0
media=0
maior=0
menor=0
while escolha == 'S' :
    num=int(input('Digite um numero: '))
    escolha=str(input('Deseja contunua[S/N]? ')).upper().strip()[0]
    soma+=num
    cont+=1
    if cont==1:
        maior=menor = num
    else:
        if num > maior:
            maior=num
        if num < menor:
            menor=num
media=soma/cont
print("""
Você digitou {} Numeros e a media foi {:.2f}, 
o maior valor foi {} e o menor foi {}""".format(cont,media,maior,menor))
