"""3)	Escreva um programa que contenha o seguinte menu:
Opção 1: Verificar e exibir se um número x é ou não divisível por 6;
Opção 2: Calcular o fatorial do número x;
Opção 3: Exibir todos os inteiros de 1 até um número x.
	O programa deverá solicitar ao usuário a leitura de um número x e a opção desejada até que o usuário digite “N”
	para encerrar o programa. OBS: o programa deverá solicitar o número e a opção enquanto o usuário digitar“S”.
"""

resp = "s"

while(resp !="n" or resp !="n"):
    num = int(input("Digite um número inteiro: "))
    print("Opção 1: Verificar e exibir se um número x é ou não divisível por 6;")
    print("Opção 2: Calcular o fatorial do número x;")
    print("Opção 3: Exibir todos os inteiros de 1 até um número x.")
    opc = int(input("Digite o a opção desejada (1 a 3): "))
    match opc:
        case 1:
            if(num % 6 == 0):
                print(f"{num} é divisivel por 6")
            else:
                print(f"{num} não é divisivel por 6")

        case 2:
            fat = 1
            for i in range(1, num + 1):
               fat *= i
            print(f"O fatoria de {num} é {fat}")

        case 3:
            for i in range(1, num + 1):
                print(i)

        case _:
            print("Opção inválida")

    resp = input("Deseja contninuar (S - Sim, N - Não): ")

