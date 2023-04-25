from flask import Flask
from flask_basicauth import BasicAuth
from googletrans import Translator
from textblob import TextBlob
import pickle

modelo = pickle.load(open('modelo.pkl','rb'))
translator = Translator()

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = 'alberto'
app.config['BASIC_AUTH_PASSWORD'] = 'alura'

basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return "Minha primeira API."

# Adicionando uma autenticação básica de usuário e senha
@app.route('/sentimento/<frase>')
@basic_auth.required
def sentimento(frase):
    frase_en = translator.translate(frase, dest='en')
    tb_en = TextBlob(frase_en.text)
    polaridade = tb_en.sentiment.polarity
    return "polaridade: {}".format(polaridade)

app.run(debug=True)