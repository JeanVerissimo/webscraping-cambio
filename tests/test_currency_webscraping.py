import unittest
from unittest.mock import patch, Mock
from data.currency_webscraping import fetch_exchange_rates

class TestCurrencyWebScraping(unittest.TestCase):

    #HTML contendo tabela válida
    @patch("data.currency_webscraping.requests.get")
    def test_fetch_exchange_rates_success(self, mock_get):
        html_mock = """
        <html>
            <body>
                <table class="tablesorter ratesTable">
                    <tr><th>Currency</th><th>Rate</th></tr>
                    <tr><td>Euro</td><td>0.85</td></tr>
                    <tr><td>British Pound</td><td>0.75</td></tr>
                </table>
            </body>
        </html>
        """

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = html_mock.encode('utf-8')
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = fetch_exchange_rates("USD")

        expected = {
            "Euro": "0.85",
            "British Pound": "0.75"
        }

        self.assertEqual(result, expected)

    #Falha na requisição
    @patch("data.currency_webscraping.requests.get")
    def test_fetch_exchange_rates_failure(self, mock_get):
        mock_get.side_effect = Exception("Erro de conexão")
        result = fetch_exchange_rates("USD", max_retries=2)
        self.assertIsNone(result)

    #Tabela correta não encontrada
    @patch("data.currency_webscraping.requests.get")
    def test_no_exchange_table_found(self, mock_get):
        html_mock = "<html><body><p>Outra tabela!</p></body></html>"

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = html_mock.encode('utf-8')
        mock_response.raise_for_status = Mock()
        mock_get.return_value = mock_response

        result = fetch_exchange_rates("USD")
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
