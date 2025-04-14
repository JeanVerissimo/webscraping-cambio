# data/currency_webscraping.py

import requests
import time
from bs4 import BeautifulSoup

def fetch_exchange_rates(base_currency, max_retries=5):
    url = f"https://www.x-rates.com/table/?from={base_currency}&amount=1"

    for attempt in range(1, max_retries + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, "html.parser")

            # A tabela de câmbio está na primeira <table class="tablesorter ratesTable">
            # Essa é a tabela com todos os câmbios em ordem alfabetica
            table = soup.find("table", class_="tablesorter ratesTable")

            exchange_rates = {}

            if table:
                rows = table.find_all("tr")[1:]  # Remover o cabeçalho
                for row in rows:
                    cols = row.find_all("td")
                    if len(cols) >= 2:
                        currency = cols[0].text.strip()
                        rate = cols[1].text.strip()
                        exchange_rates[currency] = rate


            return exchange_rates

        except Exception as e:
            print(f"[ERRO] Tentativa {attempt} falhou: {e}")
            if attempt < max_retries:
                wait_time = 2 ** attempt
                print(f"[INFO] Aguardando {wait_time}s antes da próxima tentativa...")
                time.sleep(wait_time)
            else:
                print("[ERRO] Não foi possível obter os dados do site após múltiplas tentativas.")
                return None