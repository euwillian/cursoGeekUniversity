media = 0
for i in range(10):
    n = int(input("Informe um número: "))
    if n >= 0:
        media = media + n
print(f"Média: {media / 10 }")
