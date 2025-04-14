# main.py

from datetime import datetime
from data.currency_webscraping import fetch_exchange_rates
from domain.coin_processor import process_currency_data
from infrastructure.csv_writer import write_to_csv

def main():
    print("Buscando dados de câmbio...")

    values_from_real = fetch_exchange_rates("BRL")
    values_from_dolar = fetch_exchange_rates("USD")

    #Proseguir apenas se as informações foram obtidas com sucesso
    if values_from_real is None and values_from_dolar is None:
        print("[Info] Nenhuma informação foi obtida!")
    
    else:
        #Adicionar os valores das moedas base
        values_from_real["Brazilian Real"] = 1
        values_from_dolar["US Dollar"] = 1
        
        all_data = {
            "today_BRL": values_from_real,
            "today_USD": values_from_dolar,
        }

        print("Processando dados das moedas...")
        processed_data = process_currency_data(all_data)

        print("Gerando arquivo CSV...")
        today_str = datetime.now().strftime("%d-%m-%Y")
        filename = f"moedas_webscrapping_{today_str}.csv"
        ret = write_to_csv(filename, processed_data)

        if ret:
            print(f"Arquivo gerado com sucesso: {filename}")
    


if __name__ == "__main__":
    main()
