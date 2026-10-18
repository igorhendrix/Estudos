for i in range(50, 10, -10):
    print(i)

senha = ''

while senha != '123':
    senha = input("Digite a senha: ")
    if senha == '123':
        print("Senha correta!")
