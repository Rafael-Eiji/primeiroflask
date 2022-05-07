from flask import Flask, redirect, url_for, request, Response
import requests
import json
import sqlite3


# Inicialização flask
app = Flask(__name__)

conn = sqlite3.connect('desenvolvedores.db', check_same_thread=False)

cursor = conn.cursor()

comando = "CREATE TABLE IF NOT EXISTS desenvolvedores \
        (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,\
        nome TEXT NOT NULL, \
        habilidades text)"

cursor.execute(comando)
conn.commit()


class Dev():
    def __init__(self, nome, habilidade):
        self.nome = nome
        self.habilidade = habilidade
    
    def adddev(self):
        cursor.execute("INSERT INTO desenvolvedores(nome, habilidades) VALUES (?,?)", (self.nome, self.habilidade)) 
        conn.commit()
        return True

@app.route("/dev/", methods = ['POST'])
def AddDesenvolvedor():
    retorno = json.loads(request.data)
    desenvolvedor = Dev(retorno['nome'], retorno['habilidades'] )
    desenvolvedor.adddev()
    return Response(json.dumps({'message': 'sucesso'}),mimetype='application/json'), 200 

@app.route("/dev/", methods = ['GET'])
def traztudo():
    cursor.execute("SELECT * from desenvolvedores")
    conn.commit
    retornobd = cursor.fetchall()
    return Response(json.dumps(retornobd),mimetype='application/json'), 200 

@app.route("/dev/<int:id>", methods = ['GET'])
def trazum(id):
    cursor.execute("SELECT * from desenvolvedores where id =" + str(id) )
    conn.commit
    retornobd = cursor.fetchall()
    return Response(json.dumps(retornobd),mimetype='application/json'), 200 

@app.route("/dev/<int:id>", methods = ['DELETE'])
def deletadev(id):
    cursor.execute("DELETE from desenvolvedores where id =" + str(id) )
    conn.commit
    cursor.execute("SELECT * from desenvolvedores")
    conn.commit
    retornobd = cursor.fetchall()
    return Response(json.dumps(retornobd),mimetype='application/json'), 200 

@app.route("/dev/<int:id>", methods = ['PUT'])
def AlterarDesenvolvedor(id):
    retorno = json.loads(request.data)
    cursor.execute("UPDATE desenvolvedores SET nome = ?, habilidades = ? WHERE id = ?" , (retorno['nome'], retorno['habilidades'], id))
    conn.commit()
    cursor.execute("SELECT * from desenvolvedores")
    conn.commit
    retornobd = cursor.fetchall()
    return Response(json.dumps(retornobd),mimetype='application/json'), 200 


if __name__ == '__main__':
    app.run(debug=True)