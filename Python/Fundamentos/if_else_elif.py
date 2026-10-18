numero = int(input("Digite sua idade: "))

if numero >= 18:
    print('Pode tirar carteira!')
elif numero >= 16 and numero < 18:
    print('Quase pode tirar carteira!')
else:
    print('Vai ter que esperar mais!')