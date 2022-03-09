from time import sleep 
def linha():
    print('-='*20)
    
linha()
print('Contagem de 1 até 10 de 1 em 1 ')
for c in range (1,11):
    sleep(0.3)
    print(c, end=' ', flush=True)
print('FIM!')
linha()
print('Contagem de 10 até 0 de 2 em 2 ')
for c in range (10,-2,-2):
    print(c, end=' ', flush=True)
    sleep(0.3)
print('FIM!')
linha()
inicio=int(input('Inicio '))
fim=int(input('Fim '))
passo=int(input('Passo '))
if passo == 0:
    passo=1
if fim<inicio:
    passo =- passo
for c in range(inicio, fim-1, passo):
    sleep(0)
    print(c,end=' ')
