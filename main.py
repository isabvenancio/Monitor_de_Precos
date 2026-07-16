from produtos import produtos
from scraping import pegar_preco
from historico import salvar_historico
from notificacoes import enviar_email

def verificar():

    for p in produtos:

        preco = pegar_preco(p["url"])

        salvar_historico(p["nome"], preco)

        if preco <= p["preco_desejado"]:

            enviar_email(p["nome"], preco)


verificar()