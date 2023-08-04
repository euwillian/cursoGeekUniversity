num = int(input("Informe um número: "))

for i in range(1, num):
    if (i % 2) != 0:  # Verifica se o resto da divisão é diferente de zero pois, caso seja zero o número é par.
        print(i)
