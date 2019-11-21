from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
 
def welcome_to_moringa(name,receiver):
    subject = 'You are welcome to Join Moringa School Access'
    sender = 'wachirabeatice2020@gmail.com'

    text_content = render_to_string('email/welcomeemail.txt',{'name':name})
    html_content = render_to_string('email/welcomeemail.html',{'name':name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()


def know_more(name,receiver):
    subject = 'To know more about Moringa'
    sender = 'wachirabeatice2020@gmail.com'

    #passing in the context vairables
    text_content = render_to_string('email/more.txt',{"name": name})
    html_content = render_to_string('email/more.html',{"name": name})

    msg = EmailMultiAlternatives(subject,text_content,sender,[receiver])
    msg.attach_alternative(html_content,'text/html')
    msg.send()
