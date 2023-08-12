n = int(input("Quantos números: "))
i = int(input("Valor para i: "))
j = int(input("Valor para j: "))

while True:  #  Verificar se as variáveis forem zero.
    if i == 0:
        i = int(input("Informe o valor de i, diferente de zero: "))
    elif j == 0:
        j = int(input("Informe o valor de j, diferente de zero: "))
    else:
        break

c = 0
parada = 0

while True:
    if c % i == 0 or c % j == 0:  # Valor deve ser multiplo de 'i' ou de 'j' ou de 'ambos'
        print(c)
        parada += 1  # Essa variável controla quantas interações serão mostradas, ou seja se n = 6 irá mostar 0,2,3,4,6,8, se for n=2 irá mostrar 0,2

    c += 1

    if parada == n:
        break
