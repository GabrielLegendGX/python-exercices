tabela=('Flamengo','Internacional','Atletico-MG','São Paulo','Fluminese',
'Gremio','Palmeiras','Santos','Athetico-PR','Bragantino','Ceará-GO','Bahia',
'Sport Recife','Fortaleza','Vasco da Gama','Goiás','Coritiba','Botafogo')
print('Os 5 primeiros colocados são')
print(tabela[:5])
print('-'*140)
print('Os 4 ultimos colocados são')
print(tabela[-5:])
print('-'*140)
print('Em ordem algabetica')
print(sorted(tabela))
print('-'*140)
print('O time Bragantino esta na posição')
print(tabela.index('Bragantino')+1)