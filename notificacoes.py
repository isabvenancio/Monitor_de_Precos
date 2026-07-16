import smtplib
from email.mime.text import MIMEText

def enviar_email(produto, preco):

    email = "seuemail@gmail.com"
    senha = "suasenha"

    msg = MIMEText(f"{produto} está por R${preco}")

    msg["Subject"] = "Promoção!"
    msg["From"] = email
    msg["To"] = email

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(email, senha)

    servidor.send_message(msg)

    servidor.quit()