frutas = [ "abacaxi", "abacate", "limão", "laranja", "banana", "melancia" ]
alergia = ["morango"]

#solicitar a fruta desejada com um lower para padrão
comerfruta = input("Digite a fruta que você gostaria de comer: ").lower()

#verificar se a fruta esta em alergia
if comerfruta in alergia:
    print(f"ATENÇÃO! Você não pode comer {comerfruta}!")
else: 
    #adiciona a lista de frutas caso não tenha.
    if comerfruta not in frutas:
        frutas.append(comerfruta)
    else:
         print(f"{comerfruta} foi adicionado(a) a lista de frutas.")        

#Mostrar lista atualizada!
print("Lista de frutas atual!", frutas)