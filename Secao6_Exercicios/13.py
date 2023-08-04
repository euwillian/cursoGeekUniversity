num = int(input("Informe um número: "))

for i in range(0, num + 1):  # Imprima os números pares, em ordem crescente
    if i % 2 == 0:
        print(i)
