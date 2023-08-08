inicio = int(input("Digite o primeiro número: "))
fim = int(input("Digite o primeiro número: "))

if fim < inicio:  # Essa verificação é necessária para que não ocorra casos onde o fim seja menor que o inicio
    aux = inicio
    inicio = fim
    fim = aux

soma_pares = 0
multiplicacao_impares = 1  # Não pode iniciar com zero pois, qualquer número multiplicado por zero é zero.

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma_pares += i
    else:
        multiplicacao_impares *= i

print(f"Soma pares: {soma_pares}")
print(f"Multiplicacao dos impares: {multiplicacao_impares}")
