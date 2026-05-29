# Calculadora simples
# Contas de adição, subtração, multiplicação e divisão
# Apenas para números inteiros

# Lendo os números separados por espaço e convertendo para inteiro
entrada = input("Digite os numeros da conta separados por espaco: ")
num1, num2 = map(int, entrada.split())

# Lendo o operador
operador = input("Digite o operador (+, -, *, /): ")

# Estrutura equivalente ao switch do C
if operador == '+':
    print(f"Resultado: {num1 + num2}")
elif operador == '-':
    print(f"Resultado: {num1 - num2}")
elif operador == '*':
    print(f"Resultado: {num1 * num2}")
elif operador == '/':
    if num2 != 0:
        # Usamos // para garantir que a divisão seja inteira, igual ao C
        print(f"Resultado: {num1 // num2}")
    else:
        print("Divisao por zero não existe!")
else:
    print("Operador invalido.")
