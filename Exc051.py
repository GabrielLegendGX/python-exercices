primeiro=int(input('Digite o primeiro termo: '))
razão=int(input('Razão: '))
decimo= primeiro + (10-1) * razão
for c in range (primeiro,decimo,razão ):
    print((c),end=' -> ')
print('Cabo')
