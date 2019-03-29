import json, requests


def index():
    global UF
    UF = input("Digite o codigo da UF: ")
    UFs = str("{0}".format(UF))
    r = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/"+UF+"/mesorregioes")
    if r.status_code == 200:
        data = r.json()
        print(data)
        dadospri = ("Dados{0}.txt".format(UF)) 
        dadosseg = ("Dados"+UFs+".json")
        f = ("{0}".format(dadospri))
        """for a in data:"""
        with open("{0}".format(f),"w+", encoding='utf-8') as outfile:
            json.dump(data, outfile)
            outfile.write('\n')
        print("Pronto!")
        
index()

        
    



    



