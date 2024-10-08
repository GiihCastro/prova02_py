try:
    numero = float(input("Digite um número: "))

    if numero > 0:
        mensagem = "O número é positivo."
    elif numero < 0:
        mensagem = "O número é negativo."
    else:
        mensagem = "O número é zero."

    print(f"{mensagem}")

except ValueError:
    print("Por favor, insira um número válido.")