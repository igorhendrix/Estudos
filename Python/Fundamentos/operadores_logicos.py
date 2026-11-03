# ATIVIDADE 1
def funcao1(x, y):
    teste = 'S' in resp1.upper() or 'S' in resp2.upper()

    if teste:
        print("Tem que ir ao mercado")
    else:
        print("Não tem que ir")

    return teste
print("Apenas diga sim ou não\n")

resp1 = input("Hoje é sabado? ")
resp2 = input("Falta comida? ")

bool = funcao1(resp1, resp2)

print(bool)
