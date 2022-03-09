valores=list()
for cont in range(1,6):
    valores.append(int(input('Digite um valor ')))
print(valores)
maior=max(valores)
menor=min(valores)
for pos,valor in enumerate(valores):
    if valor == maior:
        print(f'o maior valor é {maior} e esta na posição {pos+1}')
    if valor == menor:
        print(f'O valor menor é {menor} e esta na posição {pos+1}')