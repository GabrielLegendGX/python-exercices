def notas(* aluno, sit=False):
    dic=dict()
    dic['Quantidade']=len(aluno)
    dic['Maior']=max(aluno)
    dic['Menor']=min(aluno)
    dic['Media']=sum(aluno)/dic['Quantidade']
    print(dic)
    if sit == True:
        if dic['Media'] == 6 or dic['Media'] == 5:
            print('Razoavel')
        if dic['Media'] >6:
            print('Exelente')
        if dic['Media'] <4 or dic['Media'] >4:
            print('Pessimo')

resp=notas(1,10, sit=True)


#Quantidade de notas, len
#maior nota
#menor nota 
#Media da turma
#situação opcional