from flask import Flask, request, jsonify, json
from APIIBGE import APIIBGE

app = Flask(__name__)
@app.route("/busca_UFs/", methods=['GET'])

def busca_UFs():
	dados_UFs = APIIBGE()
	dic = {}
	dados = dados_UFs.UFs()
	dic['dados'] = dados
	return jsonify(dic)

@app.route("/busca_munUF/<UF>", methods=['GET'])
def busca_munUFs(UF):
	dados_munUF = APIIBGE()
	dic = {}
	dados = dados_munUF.munUF(UF)
	dic['dados'] = dados
	return jsonify(dic)

@app.route("/transforma_txt/<UF>", methods=['GET'])
def transforma_txt(UF):
        txt = APIIBGE()
        txt.transforma_txt(UF)
        return ("Pronto!")




app.run(use_reloader=True)
