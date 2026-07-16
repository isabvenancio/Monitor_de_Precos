import requests
from bs4 import BeautifulSoup
from plyer import notification
import time

# URL do produto
url = "COLE_A_URL_DO_PRODUTO_AQUI"

# preço que você deseja pagar
preco_desejado = 500,0


def verificar_preco():
    resposta = requests.get(url)
    soup = BeautifulSoup(resposta.text, "html.parser")

    preco = soup.find("span", class_="price")

    if preco:
        preco_texto = preco.get_text().replace("R$", "").replace(".", "").replace(",", ".")
        preco_valor = float(preco_texto)

        print("Preço atual:", preco_valor)

        if preco_valor <= preco_desejado:
            notification.notify(
                title="Produto em promoção!",
                message=f"O produto está custando R${preco_valor}",
                timeout=10
            )

while True:
    verificar_preco()
    time.sleep(3600)  # verifica a cada 1 hora