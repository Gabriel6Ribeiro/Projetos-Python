from Class_veiculo import veiculo

resp = "S"
while True:
    try:
        veiculo1 = veiculo(str(input("Digite a marca do veículo:")))
        veiculo1.modelos(str(input("Digite o modelo no veículo:")))
        veiculo1.anos(int(input("Digite o ano do veículo:")))
        veiculo1.valores(float(input("Digite o valor do veículo:")))
        resp = str(input("Deseja continuar?")).strip().upper()[0]
        if resp == "N":
            break
    except (ValueError, TypeError, NameError, SyntaxError, IndexError, Exception) as e:
        print(f'O erro específico foi:{e}')


print(f"Marca do veículo...:{veiculo1.marca}")
print(f"Modelo do veículo...:{veiculo1.modelo}")
print(f"Ano do veículo...:{veiculo1.ano}")
print(f"Valor do veículo...:{veiculo1.valor}")
