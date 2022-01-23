from flask import Blueprint, render_template, request
from src.controller.controller_mail import SendMail


eumeca_blueprint = Blueprint('eumeca', '__name__', template_folder='templates')


@eumeca_blueprint.route('/')
def index():
    return render_template('index.html')


@eumeca_blueprint.route('/time')
def time():
    return render_template('time.html')


@eumeca_blueprint.route('/contatos', methods=('GET', 'POST'))
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


@eumeca_blueprint.route('/servicos')
def servicos():
    return render_template('servicos.html')


@eumeca_blueprint.route('/parceiros')
def parceiros():
    return render_template('parceiros.html')


@eumeca_blueprint.route('/sobre')
def about():
    return render_template('about.html')
