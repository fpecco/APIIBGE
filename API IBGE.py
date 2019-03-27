import json, requests


def index():
    global UF
    UF = input("Digite o codigo da UF: ")
    r = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/"+UF+"/mesorregioes")
    if r.status_code == 200:
        data = r.json()
        datal = [data]
        print(data)
        for a in data:
            with open('Dados.json', 'w') as outfile:
                json.dump(a, outfile)
                outfile.write('\n')
            with open('Dados.txt', 'w') as outfile:
                json.dump(a, outfile)
                outfile.write('\n')
        print("Pronto!")
        
"""
def getmesorregiao():
    global UF
    UF = int(input("Digite o codigo da UF: "))
    response = requests.get("URL{servicodados.ibge.gov.br/api/v1/localidades/estados/UF/mesorregioes}".format(UF))
    content = '''
    [
     {
      "id":"number"
      "nome":"string"
      "UF":{
           "id":"number"
           "nome":"string"
           "sigla":"string"
        "regiao":{ }
    ]'''
    
"""

index()

        
    



    



