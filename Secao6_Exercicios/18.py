num = int(input("Informe a qntd de números a serem lidos: "))
numero_maior = 0
cont = 0

for i in range(1, num + 1):
    numero_digitado = int(input(f"Informe o {i}º número: "))
    if numero_digitado < 0:  # Validação números negativos
        print(f"Número inválido, digite um número positivo!")

    if numero_digitado > numero_maior:
        numero_maior = numero_digitado  # Atribui o maior número a variável
        cont = 1  # Conta 1
    elif numero_digitado == numero_maior:
        cont += 1  # contador de quantas vezes foi digitado o maior número

print(f"O maior número digitado foi {numero_maior} \ne foi digitado {cont} vezes!")
