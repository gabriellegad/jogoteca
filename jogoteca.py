from flask import Flask, render_template

app = Flask(__name__)

lista = ['Detroid Become Human', 'Resident Evil Village', 'uncharted the lost legacy']

@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Meus Jogos', jogos = lista)

app.run()