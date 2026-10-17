nome = input('Qual é o seu nome? ')
idade = int(input('Qual é a sua idade? '))

print("Olá", nome, "você tem", idade, "anos de idade.")

#f-string FACILITA AO ESCREVER VARIAVEIS DENTRO DE UMA STRING

print(f"Olá {nome}, você tem {idade + 5} anos de idade.")
