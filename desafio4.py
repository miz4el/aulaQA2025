nome=input("Digite seu nome: ")
nome_pet=input("Digite o nome do seu pet: ")
idade_pet=int(input("Digite a idade do seu pet, inserir apenas numeros: "))
idade_pet1=(idade_pet*7)
print(f"OLA {nome}, bem vindos a PETSHOPZELAR, ficamos contentes em rever o seu lindo pet {nome_pet}!!!!")
print(f"de acordo com a idade informada, o(a) {nome_pet} hoje tem aproximadamente {idade_pet1} anos, legal né !?")
porte_pet= input(f"Qual o porte do seu cachorro? Lembrando que trabalhamos com pequeno, médio e grande porte.")
banho_pet= int(input(f"Qual a quantidade de banhos que o {nome_pet} tomou nos ultimos 12 meses? Lembrando que a resposta tem que ser em numeros"))
if( 
    porte_pet=="Pequeno" or "pequeno"):
    valor_banho=50
    custo=5
elif(porte_pet=="Medio" or "medio"):
    valor_banho=60
    custo=15
elif(porte_pet=="Grande" or "grande"):
    valor_banho=75
    custo=20

lucro= ((valor_banho-custo)*banho_pet)

print(f"Ola {nome}, o seu pet {nome_pet} tomou banho {banho_pet} vezes, com isso o lucro com ele foi de: {lucro:.2f} reais ")