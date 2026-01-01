import re

def validar_email(email):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(regex, email):
        print(f"{email} - Email validado")
    else:
        print(f"{email} - Email invalido")

validar_email("contato@ackercode.com")