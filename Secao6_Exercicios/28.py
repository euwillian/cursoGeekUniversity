num = int(input("Informe um número: "))
e_sum = 1

for i in range(1, num + 1):
    f = 1 # Calculo do fatorial do número, exemplo 5! = (5*4*3*2*1) 120
    for fatorial in range(1, i + 1):  # Este for foi criado para calcular o fatorial sem a necessidade da biblioteca math (aprendizado)
        f *= fatorial
        #print(f"fact: {fatorial}, valor:{f}, i:{i}")  # Debug do código
    e_sum += 1 / f

print(f"Valor Final: {e_sum}")
