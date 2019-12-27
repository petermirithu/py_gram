from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_welcome_email(name,receiver):
  subject="Welcome to Py_Gram."
  sender='pyramyra33@gmail.com'

  text_content=render_to_string('email/py_gram_email.txt',{"name":name})
  html_content=render_to_string('email/py_gram_email.html',{"name":name})

  msg=EmailMultiAlternatives(subject,text_content,sender,[receiver])
  msg.attach_alternative(html_content,'text/html')
  msg.send()
  