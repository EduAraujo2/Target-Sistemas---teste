#sequência de Fibonacc
n = int(input("Digite um número: "))

# primeiro valor
fib = [0, 1]

# calculando os valores da sequencia
while fib[-1] < n:
    fib.append(fib[-1] + fib[-2])

# aqui verifica se o numero digitado está na sequencia
if n in fib:
    print(f"{n} pertence")
else:
    print(f"{n} não pertence")
