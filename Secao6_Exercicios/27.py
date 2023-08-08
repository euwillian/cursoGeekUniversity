num = int(input("Informe um número: "))
# Com o número lido iremos apresentar o valor da serie Harmónica H(n)

soma_Harmonica = 1

for i in range(2, num + 1):
    soma_Harmonica += 1/i

print(f"Valor H(n): {soma_Harmonica:.2f}")
