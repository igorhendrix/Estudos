import os

def resgatando(saldo, resgate):

    if saldo < resgate:
        print("Saldo insuficiente!")
        return saldo
    else:
        conta = saldo - resgate
        print("Resgate feito com sucesso!\n")        
        return conta

def depositando(saldo, deposito):
    conta = saldo + deposito
    return conta

def printSaldo(saldo):
    print(f"\nSeu saldo é de R${saldo:.2f}")
