import json        # Pega a caixa mágica que sabe guardar coisas como listas (JSON)
import os          # Pega ferramentas para checar se um arquivo existe

arquivo = "frutas.json"   # Nome da nossa caixinha no computador

# Se a caixinha já existir, abrimos e tiramos a lista que está dentro
if os.path.exists(arquivo):
    with open(arquivo, "r") as f:
        frutas = json.load(f)
else:
    # Se a caixinha não existir, começamos com uma lista já com algumas frutas
    frutas = ["abacaxi", "abacate", "limão", "laranja", "banana", "melancia"]

alergia = ["morango"]   # Lista de frutas que te fazem mal

while True:
    comerfruta = input("Digite a fruta que você gostaria de comer (ou 'sair' para encerrar): ").strip().lower()

    if comerfruta == "sair":
        break

    if comerfruta in alergia:
        print(f"ATENÇÃO! Você não pode comer {comerfruta}!")
    else:
        if comerfruta not in frutas:
            frutas.append(comerfruta)
            print(f"{comerfruta} foi adicionada à lista de frutas!")
        else:
            print(f"{comerfruta} já está na lista de frutas.")

    print("\nLista de frutas atualizada:", frutas)

# Quando o usuário sai, abrimos a caixinha e guardamos a lista lá dentro
with open(arquivo, "w") as f:
    json.dump(frutas, f)

print("\nLista salva com sucesso! Até a próxima 🍍")
