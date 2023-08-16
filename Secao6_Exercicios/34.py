a = 1

while True:
    contador = 0 ## Esse contador irá resertar se o valor de a não for divisível por TODOS os números do range, quando for divisível por todos e chegar a verificação do break irá satisfazer
    for i in range(1, 21):
        if a % i == 0:
            contador += 1
    if contador == 20:
        break
    a += 1  # Incremental, para garantir qual número será o valor que é divisivel por todos de 1..20

print(f"valor: {a}")