def mostralinha():
    print('-='*40)
def maior(* num):
    maior=0
    mostralinha()
    print(f'Foram informados {len(num)} valores.')
    print(f' {num}\n {max(num)} é o maior valor.')
    mostralinha()

maior(1,6,7,5,3)
maior(5,3,5)
maior(1,9)
maior(1)