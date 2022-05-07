from flask import Flask, redirect, url_for, request, Response
import requests
import json


# Inicialização flask
app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Rafael',
    'habilidades': ['Python', 'Flask']},
    {'nome': 'teste',
    'habilidades': ['Python', 'Django']}
    
]

@app.route("/dev/<int:id>/", methods = ['GET'])
def desenvolvedor(id):
    desenvolvedor = desenvolvedores[id]
    return Response(json.dumps(desenvolvedor),mimetype='application/json'), 200

@app.route("/dev", methods = ['GET'])
def listadesenvolvedor():
    return Response(json.dumps(desenvolvedores),mimetype='application/json'), 200

@app.route("/dev/<int:id>/<string:nome>", methods = ['PUT'])
def alteradesenvolver(id, nome):
    desenvolvedor = desenvolvedores[id]
    desenvolvedor["nome"] = nome
    return Response(json.dumps(desenvolvedores),mimetype='application/json'), 200


@app.route("/dev/<int:id>/", methods = ['DELETE'])
def deletadev(id):
    desenvolvedores.pop(id)
    return Response(json.dumps(desenvolvedores),mimetype='application/json'), 200

@app.route("/dev/", methods = ['POST'])
def AddDesenvolvedor():
    retorno = json.loads(request.data)
    desenvolvedores.append(retorno)
    return Response(json.dumps(desenvolvedores),mimetype='application/json'), 200

if __name__ == '__main__':
    app.run(debug=True)
