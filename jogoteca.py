from flask import Flask, render_template

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

jogo1 = Jogo('Detroid Become Human', 'Ação e Aventura', 'Playstation')
jogo2 = Jogo('Resident Evil Village', 'Survival horror ', 'Playstation')
jogo3 = Jogo('uncharted the lost legacy', 'ação-aventura', 'Playstation')

lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)
@app.route('/inicio')
def ola():
    return render_template('lista.html', titulo='Meus Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')
    
app.run()