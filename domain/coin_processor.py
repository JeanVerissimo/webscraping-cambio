# domain/coin_processor.py 

from datetime import datetime
from config.currency import CURRENCIES

def process_currency_data(data):
    """
    Processa os dados das moedas com base em BRL e USD.
    Retorna uma lista de dicionários contendo as informações formatadas para o CSV.
    """

    processed = []
    BRL = data["today_BRL"]
    USD = data["today_USD"]

    for currency in CURRENCIES:
        cod = currency[0]
        eng_name = currency[1]
        name_currency = currency[2]

        value_BRL = BRL[eng_name]
        value_USD = USD[eng_name]
        
        if value_BRL is None or value_USD is None:
            continue  # Ignora moedas que não existem em currency.py

        processed.append({
            "moeda": name_currency,
            "codigo": cod,
            "valor_em_reais": value_BRL,
            "valor_em_dolar": value_USD,
            "data_consulta": datetime.now().strftime("%d-%m-%Y"),
        })

    return processed
