from faker import Faker
import pandas as pd
import csv
#IMPORTANDO FAKER E CSV

fake = Faker()
fake = Faker('pt_BR')
#UTILIZANDO 2 VARIAVEIS, UMA PRA TRAZER A TRADUÇÃO E A OUTRA PRA "LINKAR" O PYTHON A BIBLIOTECA.
 
nome = fake.name()
#TRAZER UM NOME "FAKER" PARA A VARIAVEL NOME
nascimento = fake.date_of_birth(minimum_age=18, maximum_age=65)
#TRAZER UMA DATA DE NASCIMENTO COM UM MINIMO DE 18 ANOS E MAXIMO DE 65 ANOS
idade = (2025 - nascimento.year)
#TRAZER UMA IDADE COLOCANDO OS PARAMETROS ( ANO ATUAL - DATA DE NASCIMENTO)
cidade = fake.city()
#TRAZER A CIDADE "FAKER" UTILIZANDO UMA VARIAVEL
print(nome, cidade, idade)
#PRINTAR UM NOME,CIDADE E IDADE DO FAKER
 
def criar_persona_lista():
    #AQUI EU CRIO UMA FUNÇÃO QUE IRÁ CRIAR UMA LISTA DE PERSONAS "FAKER"
    persona_lista = []
    #CRIO UMA LISTA DE NOMES PARA OS "FAKER", NO MOMENTO ELA TA VAZIA!!!
 
    for i in range(15):
        nome = fake.name()
        persona_lista.append(nome)
        #PARA CADA "RODADA" IRÁ ADICIONAR UM NOME "FAKER" A LISTA (PERSONA_LISTA) CRIADA!!!!
    return (persona_lista) 
    #TE FAZ RETORNAR A LISTA "FAKER"
 
print (criar_persona_lista())
#PRINTAR NA TELA A FUNÇÃO

from faker import Faker
import csv
 
# Criando uma instância do Faker
fake = Faker('pt_BR')
 
 
def criar_personas(num_personas=15):
    personas = []  # Lista para armazenar as personas
 
    for _ in range(15):
        persona = {
            "nome": fake.first_name() + " " + fake.last_name(),            # Nome da persona sem sr e sra
            "email": fake.email(),          # Email da persona
            "data_nascimento": fake.date_of_birth()  # Data de nascimento
        }
        personas.append(persona)  # Adiciona o dicionário à lista
 
    return personas  # Retorna a lista de personas
 
def exportar_para_csv(personas, nome_arquivo='personas.csv'):
    caminho = r"C:\Users\Dione\Desktop\Aula_QA_2025\Atv 05 - Massa de teste\personas.csv"
    with open(nome_arquivo, mode='a', newline='', encoding='utf-8') as arquivo_csv:
        writer = csv.DictWriter(arquivo_csv, fieldnames=personas[0].keys())
        writer.writeheader()
        for persona in personas:
            writer.writerow(persona)
           
# Gerando as personas
lista_personas = criar_personas()
 
# Exportando para um arquivo CSV
exportar_para_csv(lista_personas)
 
print("Personas criadas e exportada para 'personas.csv' com sucesso!")