def discount(price, disc):
    return price * (1 - (disc/100))


preco = int(input('Digite o preço: R$'))
desconto = int(input('Digite o desconto: '))

print(f"O valor final é: R${discount(preco, desconto):.2f}")