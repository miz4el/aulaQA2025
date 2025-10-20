#Desafio Pet

# Entrada de dados
nome_pet = input('Digite o nome do seu pet: ')
idade_humana = int(input('Digite a idade humana do seu pet: '))
porte = input('Informe o porte do cachorro (pequeno, médio ou grande): ').lower()
banhos_ano = int(input('Quantos banhos ele toma por ano?'))

# Calculo da idade em anos de cachorro
idade_cachorro = idade_humana * 7

# Defnir valores de acordo com o porte
# COMITA ESSA PORRA AQUI ENTÂO
if porte == 'grande':
    valor_banho = 75
    custo_banho = 20
elif porte == 'médio':
    valor_banho = 60
    custo_banho = 15
elif porte == 'pequeno': 
    valor_banho = 50
    custo_banho = 5

else:
    print('Porte inválido! Informe pequeno, médio ou grande. ')
    exit()

# Calculo do lucro anual

lucro = (valor_banho - custo_banho) * banhos_ano

print(f'Olá, {nome_pet} tem {idade_cachorro} anos e nos últimos 12 meses o lucro com este auau foi de  R${lucro:.2f}.')