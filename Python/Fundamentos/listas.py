frutas = ['abacate', 'maçã', 'melancia']

print(*frutas)
print(", ".join(frutas))

frutas.append('banana')
frutas.remove('maçã')

print(*frutas)
print(len(frutas))

meses = ('Janeiro', 'Fevereiro', 'Março') ## TUPLAS são imutáveis