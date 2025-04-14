# config/currency.py

"""
Para adicionar novas moedas utilize o seguinte formato:
    - O primeiro índice é o código da moeda no padrão ISO (ex: "BRL")
    - O segundo índice é nome da moeda em ingles
        conforme o site https://www.x-rates.com (ex: "Brazilian_Real")
    - O terceiro índice é o nome da moeda em portugues (ex: "Real")
"""

CURRENCIES = [
    ["BRL", "Brazilian Real", "Real"],
    ["USD", "US Dollar", "Dólar Americano"],
    ["EUR", "Euro", "Euro"],
    ["GBP", "British Pound", "Libra Esterlina"],
    ["JPY", "Japanese Yen", "Iene Japonês"],
    ["CNY", "Chinese Yuan Renminbi", "Yuan Chinês"],
]
