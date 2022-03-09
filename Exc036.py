casa=float(input('Valor da casa R$ '))
salario=float(input('Seu salario R$ '))
anos=int(input('Quantos anos de financiamento? '))
p=casa / (12*anos)
minimo=salario * 30 / 100
print('Para pagar uma casa de {} em {} anos a prestação será'.format(casa,anos,p))
if p <= minimo:
    print('Emprestimo pode ser feito')
else:
    print('Emprestimo Não pode ser feito')