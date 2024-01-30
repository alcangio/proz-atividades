def calculadora(numero1, numero2, operacao):
    '''Calculadora com entrada de números e operações pelo usuário.
    Função em loop até que o usuário escolha a opção sair.'''
    if operacao == "1":
        resultado = numero1 + numero2
    elif operacao == "2":
        resultado = numero1 - numero2
    elif operacao == "3":
        resultado = numero1 * numero2
    elif operacao == "4":
        resultado = numero1 / numero2
    else:
        resultado = 0
    return resultado


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite '1' para Soma, '2' para Subtração, '3' para Multiplicação ou '4' para Divisão: ")

calculo = round(calculadora(numero1, numero2,operacao),2)
print(calculo)