nome=str(input('Digite seu nome-> ')).strip()
nome1=nome.split()
nome2=nome.rsplit()
print('muito prazer em te conhecer\n seu primeiro nome é {} \n e seu ultimo nome é {}'.format(nome1[0],nome2[-1]))