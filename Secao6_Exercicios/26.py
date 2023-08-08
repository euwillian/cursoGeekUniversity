num = int(input("Informe um número: "))
num += 1

while True:
    if num % 11 == 0:
        print(f"Número divisível por 11 - {num}")
        break
    elif num % 13 == 0:
        print(f"Número divisível por 13 - {num}")
        break
    elif num % 17 == 0:
        print(f"Número divisível por 17 - {num}")
        break
    else:
        num += 1
