km=float(input('Digite a distancia da viagem: '))
if km > 200 :
    total= km * 0.45
    print('Você vai pagar R${} para essa viagem'.format(total)) 
else:
    total= km * 0.50
    print('Você vai pagar R${} para essa viagem'.format(total))
#ate 200km = 0,50 centavos o km
# dps é 45 por km