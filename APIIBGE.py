import json, requests

class APIIBGE: 

    #Função para obter todas as Unidades da Federação.    
    def UFs(self):
        #Request no endereço da API do IBGE para od ids das UFs do Brasil.
        r = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")
        #Verifica se funcionou.
        if r.status_code == 200:
            #Armazena os dados obtidos na variavel.
            data = r.json()
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
            data = r.json()
            dic = []
            dic.append(data)
            return dic

        
    def transforma_txt(self,UF):
        self.UF = str("{0}".format(UF))
        r = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/"+UF+"/mesorregioes")
        if r.status_code == 200:
            data = r.json()
            print(data)
            dadospri = ("Dados{0}.txt".format(UF)) 
            dadosseg = ("Dados"+UF+".json")
            f = ("{0}".format(dadospri))
            with open("{0}".format(f),"w+", encoding='utf-8') as outfile:
                json.dump(data, outfile)
                outfile.write('\n')
            return



    



