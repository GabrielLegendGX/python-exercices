num = str(input('Digite um número: ')).rjust(4, '0')
print("""Unidade: {}
Dezena: {}
Centena: {}
Milhar: {}
""".format(num[3], num[2], num[1], num[0]))