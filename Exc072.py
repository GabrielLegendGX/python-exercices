numeros='Zero','Um','Dois','Tres','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte'
while True:
    usu=int(input('Digite um numero de 0 a 20.'))
    print(numeros[usu])
    if 0<= usu <=20:
        break
