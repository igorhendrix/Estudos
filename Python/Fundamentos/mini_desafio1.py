

print("Olá, seja bem-vindo ao programa de cálculo de porções de comida!")

porcao = float(input("Quantos gramas tem cada porção de comida? "))
comprou = float(input("Quantas porções de comida você comprou? "))
qtd_dia = float(input("Quantos gramas você consome por dia? "))

dio = (porcao*comprou)/qtd_dia

print(f'Você terá {dio:.1f} dias de comida.')

