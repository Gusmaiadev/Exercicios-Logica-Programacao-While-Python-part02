"""1)	Desenvolva um programa que solicite ao usuário números positivos até que o valor 0 seja pressionado.
Em seguida, calcule a média aritmética de todos os números recebidos (exceto o número 0). Além disso, apresente
o maior e o menor número digitado."""


num = int(input("Digite um número: "))

menor = num
maior = 0
media = 0
cont = 0

while(num>0):
    media += num
    if(num>maior):
        maior = num
    if(num<menor):
        menor = num

    cont+=1
    media = media / cont
    num = int(input("Digite um número: "))

print(f"A média dos números é {media:.2f}")
print(f"O maior número é {maior}")
print(f"O menor número é {menor}")

