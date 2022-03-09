print('CALCULE O SEU IMC')
peso=float(input('Qual é o seu peso? '))
altura=float(input('Qual é a sua altura? '))
imc=peso/(altura*altura)
if imc<=18.5:
    print('Abaixo do peso')
elif imc>=25:
    print('Peso ideal')
elif imc>=30:
    print('Sobre peso')
else:
    print('OBESIDADE MÓRBIDA CUIDADO')
#MENOS 18.5 ABAIXO DO PESO
#ENTRE 18.5 E 25 PESO IDEAL
#DE 25 ATÉ 30 SOBREPESO
#ACIMA DE 40 OBESIDADE MÓRBIDA