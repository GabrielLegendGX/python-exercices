maior=0
menor=0
for c in range (1,8):
    pessoa=int(input('Digite o ano que a {} pessoa nasceu '.format(c)))
    idade= 2021 - pessoa
    if idade >=21:
        maior +=1
    else:
        menor +=1
print('Ao todo tivemos {} pessoas maiores de idade\nE {} menores de idade '.format(maior, menor))