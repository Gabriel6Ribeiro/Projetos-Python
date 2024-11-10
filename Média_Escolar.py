#FUNÇÕES
def alunos(nome):
    print("-=" * 15)
    print(f"FICHA DO ALUNO: {nome}")


def nota_materias(nota1, nota2):
    return nota1 + nota2


def media_notas():
    if media >= 7:
        print(f"Situação do Aluno {nome}: Aprovado!")
    elif media >= 5 and 7:
        print(f"Situação do Aluno {nome}: Recuperação!")
    else:
        print(f"Situação do Aluno {nome}: Reprovado!")


# FUNÇÃO PRINCIAL:
continuar = "S"
while True:
    try:
        nome = str(input("Digite o nome do aluno: "))
        nota1 = float(input('Digite a 1ª nota: '))
        nota2 = float(input('Digite a 2ª nota: '))
        continuar = str(input("Deseja continuar? ")).strip().upper()[0]
        if continuar == "N":
            break
        else:
            print("Por favor responda [S/N]")
    except ValueError:
        print("Erro devido a String ao invés de numérico!")

media = (nota1 + nota2) /2

alunos(nome)
print(f"1ª nota= {nota1} 2ª nota= {nota2}, Média Final= {media}")
nota_materias(nota1, nota2)
media_notas()
