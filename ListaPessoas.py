from tkinter import N

import ast
from xml.dom import NoModificationAllowedErr
listadepessoas=list()
def menu():
    while True:
        print('\033[35m[1]Ver pessoas cadastradas\033')
        print('\033[35m[2]Cadastrar nova pessoa\033')
        print('\033[35m[3]Sair do sistema\033')
        x=input('\033[36mOpção \033')
        try:
            if x.isnumeric()==True:
                print('=-'*20)
                
            else: 
                print('\033[1;37;41mColoque uma opção valida.\033[m ')
        except (KeyboardInterrupt):
            print('\033[1;37;41mO usuario preferiu não digitar esse numero.\033[m')
            break
        if x == '1':
            VerCadastrados()
        if x == '2':
            cadastro()
        if x == '3':
            break

def cadastro():
    while True:
        Pessoa=dict()
        Pessoa['nome']=str(input('Nome '))
        Pessoa['idade']=input('Idade ')
        if Pessoa['idade'].isnumeric()==True:
            #Salvando no arquivo
            arquivo=open('Cadastros.txt', 'a')
            arquivo.write(str(Pessoa))
            arquivo.write('\n')
            arquivo.close()
            
            print('=-'*20)  
        else: 
            print('\033[1;37;41mColoque uma opção valida.\033[m ')

        s=str(input('deseja continuar?[S/N]')).strip().upper()
        while s not in 'SN': 
            print('\033[1;37;41mColoque uma opção valida.\033[m ')
            s=str(input('deseja continuar?[S/N]')).strip().upper()
        listadepessoas.append(Pessoa)
        if s == 'N':
            break

def VerCadastrados():
    arquivo=open('Cadastros.txt', 'r')
    for linha in arquivo:        
        pessoastr=linha.strip()
        pessoadict=ast.literal_eval(pessoastr)
        print(f'{pessoadict["nome"]} {" "*10}  {pessoadict["idade"]}')
    arquivo.close()
