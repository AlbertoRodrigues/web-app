from flask import Flask
import pandas as pd
import pickle

app = Flask(__name__)
# Importando o modelo treinado
modelo = pickle.load(open('modelo.pkl','rb'))

## Definindo a rota básica
@app.route('/')

def home():
    return "Minha primeira API"


@app.route('/cotacao/<int:tamanho>')
def cotacao(tamanho):
    preco = modelo.predict([[tamanho]])[0]
    return str(preco)

app.run(debug=True)

