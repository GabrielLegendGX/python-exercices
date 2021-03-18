n1=float(input('Digite sua nota do primeiro bimestre ' ))
n2=float(input('Digite sua nota do segundo bimestre ' ))
n3=float(input('Digite sua nota do terceiro bimestre ' ))
n4=float(input('Digite sua nota do quarto bimestre ' ))
resu=(n1+n2+n3+n4 )
media=(resu/4)
print(media)
    
if(media >= 6.0):
    print('você foi aprovado')
elif(media >= 4.0):
    print('você esta de recuperação')
else:
    print('Você foi reprovado')
