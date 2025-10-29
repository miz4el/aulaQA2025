import requests
#IMPORTANTE A BIBLIOTECA REQUESTS

integrantes = {
    "Dione": "11633422",
    "Kaio": "11633010",
    "Cecilia": "04013001",
    "Mizael": "11630087"
}
#DEFININDO A LISTA (CHAVES "NOMES" E VALORES "CEPS").

for nome, cep in integrantes.items():
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
#PARA CADA CHAVE NOME E VALOR CEP NOS ITEMS INTEGRANTES CHECAR PELA URL!!!

    if resposta.status_code == 200:
        dados = resposta.json()
        cidade = dados.get("localidade", "cidade não encontrada")
        print(f"{nome} mora em {cidade}!!")
        #SE A REPOSTA FOR 200 (POSITIVA), EU PEGO A RESPOSTA EM JSON USANDO A VARIAVEL DADOS
        #USO A VARIAVEL CIDADE PARA USAR O GET NOS DADOS PARA PEGAR OS ITENS "LOCALIDADE" CASO POSITIVO, CASO NEGATIVO RETORNAR "CIDADE NÃO ENCONTRADA".
        #SE POSITIVO A LOCALIDADE VAI ESTAR NA VARIAVEL CIDADE
        #COM ISSO USAREMOS O PRINT PARA EXIBIR NA TELA AS INFORMAÇÕES "NOME" E "CIDADE"

    else: 
        print(f"{nome}, Dados não encontrados!")    
        #CASO A SOLICITAÇÃO FOR NEGATIVA!