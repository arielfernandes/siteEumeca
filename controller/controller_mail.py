import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendMail:
    def __init__(self, nome, email, telefone, comment, service, company):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.comment = comment
        self.service = service
        self.company = company

    def imprimi(self):
        print('Nome: ', self.nome)
        print('Email: ', self.email)
        print('telefone: ', self.telefone)
        print('comentario: ', self.comment)

    def mail_smt(self):
        # Configuração
        host = 'smtp.gmail.com'
        port = 587
        user = '<E-mail>'
        password = '<password>'
        subject_msg = f'Contato Site - {self.service} {self.company}'
        toMail = self.email

        # Criando objeto
        print('Criando objeto servidor...')
        server = smtplib.SMTP(host, port)

        # Login com servidor
        print('Login...')
        server.ehlo()
        server.starttls()
        server.login(user, password)

        # Criando mensagem
        message = f'{self.service}\n{self.company}\n{self.nome}\n{self.email}\n{self.telefone}\n{self.comment}'

        print('Criando mensagem...')
        email_msg = MIMEMultipart()
        email_msg['From'] = user
        email_msg['To'] = toMail
        email_msg['Subject'] = subject_msg
        # print('Adicionando texto...')
        email_msg.attach(MIMEText(message, 'plain'))

        # Enviando mensagem
        print('Enviando mensagem...')
        server.sendmail(email_msg['From'],
                        email_msg['To'], email_msg.as_string())
        print('Mensagem enviada!')
        server.quit()
