import smtplib
import os
import DiccionarioArgentino
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import secret

username = secret.username
password = secret.password
mail_to = secret.mail_to

def Gmail(subject = "Buen dia",from_email= f"tu hermano molesto {<username>}", to_emails=[f"{mail_to}"]):
    
    assert isinstance(to_emails, list)
    
    #Establezco la cabezera del mail, en este caso con el from to y subject me basta
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ", ".join(to_emails)
    msg["Subject"] = subject
    
    #tomo el cuerpo del mensaje de otro script
    body = DiccionarioArgentino.palabra_del_dia()

    #armo el cuerpo del msj como html asi puedo poner titulos y encabezados, si lo pondria como texto solo quedarian todas las lineas iguales
    text = f"<h1>Hola Gasty, la palabra argentina del dia de hoy es {body['titulo'].upper()}</h1> \n <h2>Segun nuestro buen amigo el diccionario Argentino significa --> {body['cuerpo']}\n\n\n<h2>Un clasico ejemplo de esto seria ---> {body['ejem']}</h2>"
    txt_part = MIMEText(text, 'html')
    msg.attach(txt_part)

    msg_str = msg.as_string()
    
    #inicializo el servidor de forma segura
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.ehlo()
    server.starttls()

    #ingreso a mi usario de gmail y mando el mail
    try:
        server.login(username, password)
    except:
        return ("usuario o contraseña incorrecta")
    server.sendmail(from_email, to_emails, msg_str)
    server.quit()


Gmail()