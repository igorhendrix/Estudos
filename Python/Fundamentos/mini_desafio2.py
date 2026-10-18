idade = int(input("Qual a sua idade: "))


if idade >= 18:
    print("Autorizado!")
else:
    autorizacao = input("Tem autorização dos pais? (s/n): ")
    if autorizacao == 's':
        print("Ok, autorizado!")
    else:
        print("Não autorizado.")
