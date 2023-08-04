num = int(input("Informe um número: "))

for i in range(1, num + 1):  # Imprima os números impares, em ordem crescente
    if i % 2 != 0:
        print(i)
