from flask import Flask, jsonify


app = Flask(__name__)

desenvolvedores = [
    {'nome': 'Rafael',
    'habilidades': ['Python', 'Flask']},
    {'nome': 'teste',
    'habilidades': ['Python', 'Django']}
    
]

@app.route("/dev/<int:id>/")
def desenvolvedor(id):
    desenvolvedor = desenvolvedores[id]
    return jsonify(desenvolvedor)

if __name__ == '__main__':
    app.run()