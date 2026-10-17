num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divisao = num1 / num2
divisao_inteira = num1 // num2
resto = num1 % num2

print(f'A soma é {soma}')
print(f'A subtração é {subtracao}')
print(f'A multiplicação é {multiplicacao}')
print(f'A divisão é {divisao}')
print(f'A divisão inteira é {divisao_inteira}')
print(f'O resto é {resto}')

print(type(divisao))