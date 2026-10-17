num1 = 10  
num2 = 20

print (num1 == num2)
print (num1 != num2)
print (num1 > num2)
print (num1 < num2)

idade = int(input("Qual sua idade? "))

verificador = idade >= 18

if verificador:
    print("Maior de idade")
else:
    print("Menor de idade")

print(type(verificador))

usuario = input("Qual seu usuario? ")
senha = input("Qual sua senha? ")

login_valido = usuario == 'adm' and senha == '123'

if login_valido:
    print('Login permitido')
else:
    print('Entrada não permitida')