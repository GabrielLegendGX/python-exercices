import Moeda
n = float(input('Digite um valor '))
print(f'Metade de R${n} é R${Moeda.metade(n)}')
print(f'O dobro de R${n} é R${Moeda.dobro(n)}')
print(f'aumentando 10% de R${n} da R${Moeda.aumenta10(n)}')
print(f'reduzindo 13% de R${n} da R${Moeda.reduz13(n)}')