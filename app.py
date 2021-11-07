from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    return render_template('time.html')


@app.route('/contatos')
def contatos():
    return render_template('contatos.html')


@app.route('/servicos')
def servicos():
    return render_template('servicos.html')


@app.route('/parceiros')
def parceiros():
    return render_template('parceiros.html')


@app.route('/sobre')
def about():
    return render_template('about.html')
