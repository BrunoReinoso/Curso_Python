from string import Template
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from dados import meu_nome, meu_email, minha_senha, nome_destinatario, email_destinatario, assunto

'''
    Essa parte carrega o arquivo html e faz as substituições de acordo com as variáveis presentes nele
'''

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    mensagem = template.substitute(destinatario=nome_destinatario, data=data_atual, remetente=meu_nome)
    print (mensagem)

'''
    Essa parte registra os campos do email que será enviado.
'''

msg = MIMEMultipart()
msg['from'] = meu_nome
msg['to'] = email_destinatario
msg['subject'] = assunto

corpo = MIMEText(mensagem, 'html')
msg.attach(corpo)

'''
    Essa parte carrega a imagem que será enviada por anexo.
'''

with open('img.png', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

'''
    Essa parte faz a conexão com os servidores da Google, no caso de enviar pelo gmail.
'''

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('Email enviado com sucesso!')
    except Exception as e:
        print('Email não enviado.')
        print('Error: ', e)