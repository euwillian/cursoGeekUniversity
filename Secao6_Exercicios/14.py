num = int(input("Informe um número: "))

for i in range(num, -1, -1):  # Imprima os números pares, em ordem decrescente
    if i % 2 != 0:
        print(i)
