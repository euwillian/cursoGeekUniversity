num = int(input("Informe um número: "))
soma = 0

for i in range(1, num ):
    if num % i == 0:
        soma += i
print(f"A soma dos divisores é {soma}")
