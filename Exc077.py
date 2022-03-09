palavras=('jack','programar','garrafa','fini','pause','caneta','cubo','carregador','bexiga')
for c in palavras:
    print(f'\nNa palavra {c} temos ',end=' ')
    for letras in c:
        if letras.upper() in 'AEIOU':
            print(f'{letras.upper()}',end=' ')