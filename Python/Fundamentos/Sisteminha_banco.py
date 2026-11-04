import os

def resgatando(saldo, resgate):
    conta = saldo - resgate
    return conta

def printSaldo(saldo):
    print(f"\nSeu saldo é de R${saldo:.2f}")


print(" ---------- Bem vindo ao Banco! ---------- ")

saldo = 10000

i=1
while i!=0:

    print("\nDigite o que deseja fazer: ")
    opcao = int(input("[1] Ver saldo atual\n[2] Resgatar dinheiro\n[0]Sair do sistema\n"))

    i = opcao

    if opcao == 1:
        os.system('cls')
        printSaldo(saldo)
        

    if opcao == 2:
        os.system('cls')
        resgate = int(input("\nQuanto deseja resgatar? "))
        saldo = resgatando(saldo, resgate)
        print("Resgate feito com sucesso!\n")
        
