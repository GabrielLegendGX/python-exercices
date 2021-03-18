nome = str(input('Qual seu nome completo ? '))
nome = nome.lower().strip().split()
find = "silva" in nome
print(find)