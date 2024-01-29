def calculadora(numero1, numero2, operacao):
    '''Calculadora de dois números com três parâmetros: os dois
    primeiros erão os números da operação e o terceiro será a
    entrada que definirá a operação a ser executada.'''
    if operacao == "1":
        resultado = numero1 + numero2
        return resultado
    elif operacao == "2":
        resultado = numero1 - numero2
        return resultado
    elif operacao == "3":
        resultado = numero1 * numero2
        return resultado
    elif operacao == "4":
        resultado = numero1 / numero2
        return resultado
    else:
        resultado = 0
        return resultado


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Digite '1' para Soma, '2' para Subtração, '3' para Multiplicação ou '4' para Divisão: ")

calculo = round(calculadora(numero1, numero2,operacao),2)
print(calculo)