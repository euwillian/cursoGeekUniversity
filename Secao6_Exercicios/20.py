parada = 0
par = 0
cont = 0

while parada != 1000:
    parada = int(input("Digite um número: "))

    if parada % 2 == 0:  # Se o resto da divisão por 2 for zero, logo o número é par
        par += 1  # Quantidade de números pares lidos
    cont += 1  # Número de dados lidos, contador

print(f'Pares: {par}\nNúmeros lidos: {cont}')
