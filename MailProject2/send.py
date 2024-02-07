
# -*- coding: utf-8 -*-
from MailSend import MailSender

# Mailconnection = 'kiatou.inc@gmail.com'
Mailconnection = 'johnyentreprise@gmail.com'
MailReciever = 'jekoka@oxyl.fr'
Subjectsss = 'Hello'


from subprocess import call
import time as tm
class CallPy(object):
    def __init__(self,path = 'quittance_loyer.py'):
        self.path = path

    def call_python_file(self):
        call(["python3", "{}".format(self.path)])

if __name__ == "__main__":
    c=CallPy()
    c.call_python_file()


def envoie(username,password,receiver,subjects):
    sender = username
    images = list()
    images.append({
        'id': 'logo',
        'path': 'ImageLoyerPython/kiatou.png'
    })

    with open('template.html') as template_html, open('template.txt') as template_plain:
        message_html = template_html.read()
        message_plain = template_plain.read()
        mail_sender = MailSender(username, password)
        mail_sender.send(sender, [receiver], subjects, message_html=message_html, message_plain=message_plain, images=images)
for i in range(1):
    envoie(Mailconnection,MailPassword,MailReciever,Subjectsss)
