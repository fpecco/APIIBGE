import json, requests

class APIIBGE: 

    #Função para obter todas as Unidades da Federação.    
    def UFs(self):
        #Request no endereço da API do IBGE para od ids das UFs do Brasil.
        r = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
        #Verifica se funcionou.
        if r.status_code == 200:
            #Cria uma variavel para o json obtido.
            data = r.json()
            #Cria um dicionario e armazena os dados
            dic = []
            dic.append(data)
            return dic



    #Função para obter os municipios por UF.
    def munUF(self, UF):
        #Request no endereço da API do IBGE para municipios por UF.
        r = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/"+UF+"/municipios")
        #Verifica se funcionou.
        if r.status_code == 200:
            #Armazena os dados obtidos na variavel.
            global data
            #Cria uma variavel para o json obtido.
            data = r.json()
            #Cria um dicionario e armazena os dados
            dic = []
            dic.append(data)
            return dic

    #Função para obter um json com os municipios da UF desejada e arquivalo em .txt.
    def transforma_txt(self,UF):
        #Transforma o parametro passado em uma variavel e formata como uma string.
        self.UF = str("{0}".format(UF))
        #Request no endereço da API do IBGE para municipios por UF.
        r = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/"+UF+"/mesorregioes")
        #Verifica se funcionou.
        if r.status_code == 200:
            #Cria uma variavel para o json obtido.
            data = r.json()
            #Armazena o nome que será dado ao arquivo .txt em uma variavel.
            dadospri = ("Dados{0}.txt".format(UF)) 
            #Formata esse nome como uma string.
            f = ("{0}".format(dadospri))
            #Cria o arquivo .txt.
            with open("{0}".format(f),"w+", encoding='utf-8') as outfile:
                #Armazena o json como txt.
                json.dump(data, outfile)
                outfile.write('\n')
            return



    



