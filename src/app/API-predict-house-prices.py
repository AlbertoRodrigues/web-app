from flask import Flask
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

df = pd.read_csv('casas.csv')
colunas = ['tamanho','preco']
df = df[colunas]

X = df.drop('preco', axis=1)
y = df['preco']

modelo = LinearRegression()
modelo.fit(X, y)

## Definindo a rota básica
@app.route('/')

def home():
    return "Minha primeira API"


@app.route('/cotacao/<int:tamanho>')
def cotacao(tamanho):
    preco = modelo.predict([[tamanho]])
    return str(preco)

app.run(debug=True)

