numero = int(input("Digite um número entre 100 ~ 999: "))

while numero < 100 or numero > 999:  # Validação
    numero = int(input("Número inválido! Digite um número entre 100 ~ 999: "))

numero = str(numero)

print(f"{numero[0]}\n{numero[1]}\n{numero[2]}")

#  Outra forma de fazer, mais simples
"""for i in str(numero): 
    print(i)"""
