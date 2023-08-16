num_inicial = int(input("Digite o número inicial: "))
num_final = int(input("Digite o número final: "))

soma_impares = 0
cont = num_inicial

while cont <= num_final:  # Condição para sair do looping
    if num_inicial > num_final:
        print('Intervalo de valores inválidos!')
        break

    for i in range(num_inicial, num_final + 1):  # Para ir até o número final + 1 (se não para em um número anterior)
        if i % 2 != 0:
            soma_impares += i
        print(f'looping {i}, valor da soma {soma_impares}, contador: {cont}')  # debug
        cont += 1  # condição para parada do looping

if soma_impares != 0:
    print(f'A soma dos valores ímpares é {soma_impares}')
