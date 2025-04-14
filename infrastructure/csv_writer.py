# infrastructure/csv_writer.py

import csv

def write_to_csv(filename: str, data: list[dict]) -> None:
    """
    Escreve os dados processados em um arquivo CSV.
    """
    if not data:
        print("Nenhum dado para escrever no CSV.")
        return

    fieldnames = list(data[0].keys())

    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)

        print(f"Arquivo CSV '{filename}' criado com sucesso.")
        return True

    except Exception as e:
        print(f"Erro ao escrever o arquivo CSV: {e}")
        return False
