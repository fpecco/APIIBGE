import json, requests
# Função para o Menu

#Função para obter as mesoregiões por UF.
def dadosNome():
    #Cria uma variável para Input da UF escolhida.
    nome = input("Digite um nome: ")
    #Transforma a variável em string.
    nomestr = str("{0}".format(nome))
    #Request no endereço da API do IBGE para mesoregiões por UF.
    r = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/{0}".format (nomestr))
    #Verifica se funcionou.
    if r.status_code == 200:
        data = r.json()
        print(data)
        #Parametro para criação de um .txt.
        dadospri = ("Dados{0}.txt".format(nome))
        #Variavel contendo o parametro de criação do arquivo.
        f = ("{0}".format(dadospri))
        #Cria um arquivo .txt e armazena os dados obtidos da API.
        with open("{0}".format(f),"w+", encoding='utf-8') as outfile:
            json.dump(data, outfile)
            outfile.write('\n')
        print("Pronto!")
        


dadosNome()        
    



    



