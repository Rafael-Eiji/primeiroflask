from cProfile import run
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {'id':0,
    'nome':'Rafael',
    'habilidade': ['Python', 'Flask']},
    {'id':1,
    'nome':'teste',
    'habilidade': ['Python', 'Django']}
]

class Desenvolvedor(Resource):
    def get(self, id):
        response = desenvolvedores[id]
        return response

api.add_resource(Desenvolvedor, '/dev/<int:id>/')


if __name__ == '__main__':
    app.run(debug = True)
