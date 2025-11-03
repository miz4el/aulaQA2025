nome = input("Digite o seu nome: ")
frequencia = int(input("Digite a sua frequencia: "))
print(f"{type(frequencia)} {frequencia}")
if frequencia >=1 and frequencia <20:
    print("VOCÊ ESTÁ PARTICIPANDO DA NOSSA PROMO TREINA JUNTO")
elif frequencia>=21: 
    print("UHUU. AGORA VOCÊ PODE PRESENTEAR UM AMIGO OU AMIGA PARA TREINAR COM VOCÊ")
else: print("QUE BOM VER VOCÊ DE VOLTA. A PARTIR DE AGORA INICIAMOS MAIS UMA CONTAGEM DE 21 DIAS PARA A PROMO TREINA JUNTO")