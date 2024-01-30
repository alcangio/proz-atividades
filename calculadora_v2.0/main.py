from art import logo
def calculadora(numero1, numero2, operacao):
    '''Função calculadora que os números e as operações serão feitas pelo usuário.
    O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair.'''
    if operacao == 1:
        resultado = numero1 + numero2
    elif operacao == 2:
        resultado = numero1 - numero2
    elif operacao == 3:
        resultado = numero1 * numero2
    elif operacao == 4:
        resultado = numero1 / numero2
    return resultado


calc_ligada = True
while calc_ligada:
    print(logo)
    operacao = int(input("1: Soma\n2: Subtração\n3: Multiplicação\n4: Divisão\n0: Sair\n\nDigite o número correspondente à opção desejada: "))
    if operacao == 0:
        calc_ligada = False
        print("Aplicação encerrada.")
    elif operacao > 4:
        print("Essa opção não existe.")
    else:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))
        calculo = round(calculadora(numero1, numero2,operacao),2)
        print(f"Resultado da operação: {calculo}\n")