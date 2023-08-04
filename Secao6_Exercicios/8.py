for i in range(10):
    numero = int(input("Informe um número: "))
    if i == 0:  # Primeira execução irei iniciar as variáveis
        maior = numero
        menor = numero
    if numero > maior:  # Verifica se é maior
        maior = numero
    if numero < menor:  # Verifica se é menor
        menor = numero

print(f"Maior: {maior} \nMenor: {menor}")
