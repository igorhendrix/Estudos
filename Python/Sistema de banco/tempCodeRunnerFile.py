import os
import Fcontas

def iniciar_interface():

    print(" ---------- Bem vindo ao Banco! ---------- ")

    saldo = 10000

    i=1
    while i!=0:

        print("\nDigite o que deseja fazer: ")
        opcao = int(input("[1] Ver saldo atual\n[2] Resgatar dinheiro\n[3]Depositar dinheiro\n[0]Sair do sistema\n"))

        i = opcao

        if opcao == 1:
            os.system('cls')
            Fcontas.printSaldo(saldo)
            
        if opcao == 2:
            os.system('cls')
            resgate = int(input("\nQuanto deseja resgatar?\nR$"))
            saldo = Fcontas.resgatando(saldo, resgate)
            
        if opcao == 3:
            os.system('cls')
            deposito = int(input("Quanto deseja depositar?\nR$"))
            saldo = Fcontas.depositando(saldo, deposito)
            print("Deposito feito!")

        if opcao == 0:
            os.system('cls')
            print("Obrigado, volte sempre!")
            break

