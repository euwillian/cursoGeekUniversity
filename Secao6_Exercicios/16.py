num = int(input("Informe um número: "))

for i in range(num + 1, -1, -1):  # Imprima os números impares, em ordem decrescente
    if i % 2 != 0:
        print(i)
