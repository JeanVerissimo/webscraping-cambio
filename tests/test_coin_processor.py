import unittest
from unittest.mock import patch
from datetime import datetime
from domain.coin_processor import process_currency_data


class TestProcessCurrencyData(unittest.TestCase):

    @patch("domain.coin_processor.CURRENCIES", [
        ["BRL", "Brazilian Real", "Real"],
        ["USD", "US Dollar", "Dólar Americano"],
        ["EUR", "Euro", "Euro"]
    ])
    def test_process_currency_data_success(self):
        mock_data = {
            "today_BRL": {
                "Brazilian Real": "1",
                "US Dollar": "5.84",
                "Euro": "6.70"
            },
            "today_USD": {
                "Brazilian Real": "0.171",
                "US Dollar": "1",
                "Euro": "0.88"
            }
        }

        result = process_currency_data(mock_data)
        
        # Verifica se result é uma lista de dicionários com as chaves corretas
        self.assertIsInstance(result, list)
        self.assertEqual(len(result), 3)

        for item in result:
            self.assertIn("moeda", item)
            self.assertIn("codigo", item)
            self.assertIn("valor_em_reais", item)
            self.assertIn("valor_em_dolar", item)
            self.assertIn("data_consulta", item)

        # Verifica valores específicos
        self.assertEqual(result[0]["moeda"], "Real")
        self.assertEqual(result[1]["codigo"], "USD")
        self.assertEqual(result[2]["valor_em_dolar"], "0.88")


if __name__ == "__main__":
    unittest.main()
