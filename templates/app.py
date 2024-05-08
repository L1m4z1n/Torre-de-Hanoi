#Aqui inportamos a biblioteca flask que ajuda-nos a trabalhar com web
from flask import Flask, render_template, request 
app = Flask(__name__)

#Configuração do jogo
def torre_hanoi(numero, inicio, auxiliar, fim):
    if numero == 1:
        return [('Muda o disco 1 da coluna {} para a coluna {}'.format(inicio, fim))]
    else:
        passos = torre_hanoi(numero - 1, inicio, fim, auxiliar)
        passos.append('Muda o disco {} da coluna {} para a coluna {} \n'.format(numero, inicio, fim))
        passos.extend(torre_hanoi(numero - 1, auxiliar, inicio, fim))
        return passos

#Rota da pagina inicial
@app.route('/')
def home():
    return render_template('home.html')

#Rota da pagina do jogo
@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        numero = int(request.form['numero'])
        passos = torre_hanoi(numero, 'A', 'B', 'C')
        return render_template('game.html', passos=passos)
    return render_template('game.html', passos=None)

#Rota da pagina da tabela
@app.route('/table')
def table():
    # Aqui você pode adicionar código para mostrar uma tabela, se necessário(vamos usar futuramente)
    return render_template('table.html')

#Inicia o servidor! Debug fica ativo para atualizar o site assim que mudar algo do codigo 
if __name__ == '__main__':
    app.run(debug=True)#-> Debug

