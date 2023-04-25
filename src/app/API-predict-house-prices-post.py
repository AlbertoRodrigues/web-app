from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'alberto'
app.config['BASIC_AUTH_PASSWORD'] = 'alura'

basic_auth = BasicAuth(app)

modelo = pickle.load(open('modelo2.pkl','rb'))
colunas = ['tamanho','ano', 'garagem']

## Definindo a rota básica
@app.route('/')

def home():
    return "Minha primeira API"

# Criando um dados a partir de um json e realizando a predição
@app.route('/cotacao/', methods=['POST'])
@basic_auth.required
def cotacao():
    dados = request.get_json()
    dados_input = [dados[col] for col in colunas]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])

app.run(debug=True)

