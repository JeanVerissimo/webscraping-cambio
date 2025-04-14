import unittest
import os
import csv
from datetime import datetime
from unittest.mock import patch, mock_open
from infrastructure.csv_writer import write_to_csv


class TestCSVWriter(unittest.TestCase):
    def setUp(self):
        self.filename = "test_output.csv"

        self.sample_data = [
            {
                "moeda": "Real",
                "codigo": "BRL",
                "valor_em_reais": "1",
                "valor_em_dolar": "5.847572",
                "data_consulta": "14-04-2025"
            },
            {
                "moeda": "Dólar Americano",
                "codigo": "USD",
                "valor_em_reais": "0.171011",
                "valor_em_dolar": "1",
                "data_consulta": "14-04-2025"
            }
        ]

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_valid_data(self):
        # Testa se os dados são salvos no CSV
        result = write_to_csv(self.filename, self.sample_data)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.filename))

        # Verifica se os dados estão corretos
        with open(self.filename, newline='', encoding='utf-8') as csvfile:
            reader = list(csv.DictReader(csvfile))
            self.assertEqual(len(reader), 2)
            self.assertEqual(reader[0]["moeda"], "Real")
            self.assertEqual(reader[1]["codigo"], "USD")
            self.assertEqual(reader[1]["valor_em_dolar"], "1")
            self.assertEqual(reader[1]["data_consulta"], "14-04-2025")

    def test_write_empty_data(self):
        result = write_to_csv(self.filename, [])
        self.assertIsNone(result)
        self.assertFalse(os.path.exists(self.filename))


if __name__ == "__main__":
    unittest.main()
