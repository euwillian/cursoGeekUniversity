media = 0  # Irá somar as notas informadas
cont = 0  # contador para calcular a média


while True:
    notas = int(input("Informe a nota: "))
    if notas < 10 or notas > 20:  # Não pode ser menor que 10 e maior que 20
        print("Nota fora dos válores válidos!")
        break
    else:
        media = media + notas
        cont = cont + 1

print(f"Média {media / cont}")
