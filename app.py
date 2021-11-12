from flask import Flask, render_template, url_for, request
from controller.controller_mail import SendMail

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/time')
def time():
    return render_template('time.html')


@app.route('/contatos', methods=('GET', 'POST'))
def contatos():
    if request.method == 'POST':
        name = request.form['inputName']
        email = request.form['inputEmail']
        phone = request.form['inputPhone']
        company = request.form['inputCompany']
        comment = request.form['inputText']
        service = request.form['inputService']

        s = SendMail(name, email, phone, comment, service, company)
        s.imprimi()
        s.mail_smt()
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
