valores=list()
while True:
    n=int(input('Digite um numero -> '))
    if n not in valores:
        valores.append(n)
        print('Esse numero foi adicionado ')
    else:
        print('Valor duplicado, não vai ser adicionado')
    continua=str(input('Deseja contunuar?(S/N)')).upper()[0]
    
    while continua not in 'SN':
        continua=str(input('Opção invalida, tente novamente (S/N)')).upper()[0]
    if continua == 'N':
        break
valores.sort()
print(valores)
