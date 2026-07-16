import pandas as pd
from datetime import datetime

def salvar_historico(nome, preco):

    dados = {
        "produto": nome,
        "preco": preco,
        "data": datetime.now()
    }

    df = pd.DataFrame([dados])

    df.to_csv(
        "historico_precos.csv",
        mode="a",
        header=False,
        index=False
    )