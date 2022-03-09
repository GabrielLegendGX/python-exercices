frase = str(input('Digite uma frase: ')).strip().upper() 
palavras = frase.split() #Separa em palavras 
junto = ''.join(palavras)#Junta todas as palavras sem espaço
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')