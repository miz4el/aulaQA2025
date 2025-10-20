#Pegar o nome do usuario
nome=input("Ola! digite o seu nome: ")

#pegar as 4 notas
nota1 = float(input("Digite sua nota na primeira prova: "))
nota2 = float(input("Digite sua nota na segunda prova: "))
nota3 = float(input("Digite sua nota na terceira prova: "))
nota4 = float(input("Digite sua nota na quarta prova: "))

#calcular a media
media1=(nota1 + nota2 + nota3 + nota4)
media=media1/4

#mensagem com o nome e a media
print(f"Ola {nome}, sua média é de {media:.1f}!!")