from flask import Flask
from textblob import TextBlob
import pandas as pd
from googletrans import Translator
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
translator = Translator()

## Definindo a rota básica
@app.route('/')

def home():
    return "Minha primeira API"

# Definindo uma rota acrescentando sentimento e a frase a ser predita, colocando ela na URL
@app.route('/sentimento/<frase>')
def sentimento(frase):
    frase_en = translator.translate(frase, dest='en')
    tb_en = TextBlob(frase_en.text)
    polaridade = tb_en.sentiment.polarity
    return "polaridade: {}".format(polaridade)

app.run(debug=True)

