import os
import Fcontas
import FgerenciadorUsuarios





def iniciar_interface():

    print(" ---------- Bem vindo ao Banco! ---------- ")

    opcao1 = int(input("[1] Fazer login\n[2] Criar conta\n"))

    if opcao1 == 1:
        if not FgerenciadorUsuarios.fazer_login():
            
    elif opcao1 == 2:
        FgerenciadorUsuarios.new_User()

    saldo = 10000

    i=1
    while i!=0:

        print("\nDigite o que deseja fazer: ")
        opcao2 = int(input("[1] Ver saldo atual\n[2] Resgatar dinheiro\n[3]Depositar dinheiro\n[0]Sair do sistema\n"))

        i = opcao2

        if opcao2 == 1:
            os.system('cls')
            Fcontas.printSaldo(saldo)
            
        if opcao2 == 2:
            os.system('cls')
            resgate = int(input("\nQuanto deseja resgatar?\nR$"))
            saldo = Fcontas.resgatando(saldo, resgate)
            
        if opcao2 == 3:
            os.system('cls')
            deposito = int(input("Quanto deseja depositar?\nR$"))
            saldo = Fcontas.depositando(saldo, deposito)
            print("Deposito feito!")

        if opcao2 == 0:
            os.system('cls')
            print("Obrigado, volte sempre!")
            break

