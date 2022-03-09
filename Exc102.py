from pickle import TRUE


def fatorial(n, show=False):
    f=1 
    for c in range(n,0,-1):
        if show:
            print(f'{c} X',end='')
        f *= c
    print(f'= {f}')
fatorial(5)
#Coloque uma virgula e True depois do numero