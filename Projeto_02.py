#Atendimento de uma recepção
def prioridade():
    resp = 'S'
    while resp in 'S/N':
        while True:
            try:
                nome = str(input('Digite o seu nome: '))
                idade = int(input('Digite sua idade: '))
                if idade >= 65:
                    print('Atendimento Prioritário!')
                    break
                elif idade < 65:
                        genero = str(input('Digite o seu Gênero:')).strip().upper()[0]
                        if genero in "F/M":
                            if genero == "M":
                                print('Atendimento SEM Prioridade!')
                                break
                            elif genero == "F":
                                gravidez = str(input('Você está grávida? ')).strip().upper()[0]
                                if gravidez in "S/N":
                                    if gravidez == "N":
                                        print('Atendimento SEM Prioridade!')
                                        break
                                    elif gravidez == "S":
                                        print('Atendimento Prioritário!')
                                        break
                                else:
                                    print("Resposta errada, Por favor responda novamente.")
                        else:
                            print("Gênero digitado errado, tente novamente.")
            except Exception as e:
                print(f'Erro: A causa do erro foi devido a: {e}')
        resp = str(input('Deseja continuar? [S/N]:')).strip().upper()[0]
        if resp == 'N':
            break
resultado = prioridade()
print(resultado)
print('FIM')