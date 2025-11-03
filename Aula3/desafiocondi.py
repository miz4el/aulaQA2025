nome = input("digite seu nome: ")
valor_compra = float(input("Digite o valor da sua compra: "))
if valor_compra <=249.99:
    print(f"Poxa {nome}, falta pouco para você ganhar 10% de desconto em sua compra!!!")
elif valor_compra <=499.99:
    print(f"Parabéns {nome}, você ganhou 10% de desconto, mas atenção, você poderá ganhar 30% em compras no valor de R$500,00!!!")
else:
    print(f"PARÁBENS {nome}!!!, Você ganhou um SUPER DESCONTO de 30%!!!!!")