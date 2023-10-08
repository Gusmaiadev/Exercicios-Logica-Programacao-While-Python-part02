"""2)	O dono de uma mercearia da zona rural do interior de SP necessita automatizar o processo de
totalização das compras de seus clientes, porém ele não tem condições financeiras para adquirir os equipamentos
necessários para leitura de códigos de barras e afins. Dessa forma, o funcionário do caixa terá que digitar os preços
dos produtos e as quantidades para que as compras dos clientes sejam totalizadas. Escreva um programa que calcule o
total da compra do cliente, sendo que o usuário deverá digitar os preços e as quantidades dos produtos e, quando a compra
 terminar, digitar 0 (zero) no valor do preço para finalizar e informar o valor a pagar ao cliente."""

cont = 1
valor_total = 0
valor_produto = 0

preco = float(input(f"Digite o valor do {cont}º produto: "))
qtd = int(input(f"Digite a quantidade comprada do {cont}º produto: "))

while(preco!=0):
    valor_produto = preco * qtd
    valor_total += valor_produto
    cont += 1
    preco = float(input(f"Digite o valor do {cont}º produto: "))
    qtd = int(input(f"Digite a quantidade comprada do {cont}º produto: "))

print(f"O valor da compra do cliente será R${valor_total:.2f}")