print("Informe seu nome completo: ")
nome_completo = input()

anoCorreto = False

while (anoCorreto == False):
    print("Informe seu ano de nascimento - compreendido entre 1922 e 2021: ")
    ano_nascimento = int(input())
    try:
        if (ano_nascimento >= 1922) and (ano_nascimento <= 2021):
            idade = 2022 - ano_nascimento
            print("Em 2022, ", nome_completo, " completou: ", idade, "anos.")
            anoCorreto = True
        else:
            raise Exception("Ano inválido. Tente novamente.")
    except Exception as e:
        print(e)