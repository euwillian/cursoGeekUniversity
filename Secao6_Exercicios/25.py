soma = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        soma += i
print(f"soma dos números naturais multiplos de 3 e 5 é {soma}")
