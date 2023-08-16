while True:

    operacao = int(input('Digita o número da opção que irá realizar:\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Saída\n>>> '))

    if operacao != 1 and operacao != 2 and operacao != 3 and operacao != 4 and operacao != 5:
        operacao = int(input('Digita o número da opção que irá realizar:\n1- Adição\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Saída\n>>> '))
    elif operacao == 5:
        break
    else:
        num1 = int(input(f'Informe o primeiro número: '))
        num2 = int(input(f'Informe o segundo número: '))

#  Operações
    if operacao == 1:
        print(f'Adição: {num1 + num2}\n')
    elif operacao == 2:
        print(f'Subtração: {num1 - num2}\n')
    elif operacao == 3:
        print(f'Multiplicação: {num1 * num2}\n')
    elif operacao == 4:
        if num2 == 0:
            print('Não pode dividir por zero!')
        else:
            print(f'Divisão: {num1 / num2}\n')
