from pydoc import doc
from flask import Flask, request
from flask_restx import Api, Resource, Namespace

app = Flask(__name__)
api = Api(app, title='Flask API', description='A simple calculator API with add and multiply operations', doc='/swagger', version='1.0')

ns = api.namespace('Calculator', description='Calculator operations')

@ns.route('/soma')
class Soma(Resource):
    @api.doc(params={'x': 'First number', 'y': 'Second number'})
    def post(self):
        data = request.get_json()
        x = float(data.get('x', 0))
        y = float(data.get('y', 0))
        return {'resultado': x + y}

@ns.route('/multiplicacao')
class Multiplicacao(Resource):
    @api.doc(params={'x': 'First number', 'y': 'Second number'})
    def post(self):
        data = request.get_json()
        x = float(data.get('x', 0))
        y = float(data.get('y', 0))
        return {'resultado': x * y}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
