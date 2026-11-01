def media():
    qtd_num = int(input("Quantos numeros deseja: "))
    numeros = []

    for i in range(0,qtd_num,1):
        valor = int(input(f"Digite o {i+1}º numero: "))
        numeros.append(valor)

    print(f"Lista final: {numeros}")
    media_final = sum(numeros)/qtd_num
    print(sum(numeros))
    
    return media_final


print(media())