#FUNÇÕES PARA ARMAZENAR OS CÁLCULOS
def somar(a, b):
    return num1 + num2


def subtrair(a, b):
    return num1 - num2


def multiplicar(a, b):
    return num1 * num2


def divisão(a, b):
    return num1 / num2


# ESCOLHA UM NÚMERO PARA QUE SEJA FEITA A OPERAÇÃO E EM SEGUIDA ESCOLHA 2 NÚMEROS PARA QUE SEJA REALIZADA.
escolha = 0
while escolha != 6:
    try:
        print('''Escolha o número das OPÇÕES abaixo:
        [1] SOMAR
        [2] SUBTRAIR
        [3] MULTIPLICAR
        [4] DIVISÃO
        [5] MAIOR
        [6] MENOR''')
        escolha = int(input('Escolha o número da opção selecionada:'))
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        if escolha == 1:
            print(f"{num1} + {num2} = {somar(num1, num2)}")
        elif escolha == 2:
            print(f"{num1} - {num2} = {subtrair(num1, num2)}")
        elif escolha == 3:
            print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
        elif escolha == 4:
            print(f"{num1} / {num2} = {divisão(num1, num2)}")
        elif escolha == 5:
            if num1 > num2:
                maior = num1
            else:
                maior = num2
            print(f"Entre {num1} e {num2} o maior é o {maior}")
        elif escolha == 6:
            if num1 < num2:
                menor = num1
            else:
                menor = num2
            print(f"Entre {num1} e {num2} o menor é o {menor}")
        else:
            print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE!')
        proxima = input("Deseja realizar outra operação? (s/n): ")
        if proxima.lower() != 's':
            print('Programa Finalizado... FIM!')
            break
    except ValueError:
        print(f"ERRO! O Problema foi devido a String ao invés de número")
    except Exception as e:
        print(f"ERRO! O Problema foi devido Divisor por zero: {e}")
