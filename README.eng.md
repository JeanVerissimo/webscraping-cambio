# Exchange Rate Web Scraping

[🇧🇷 Leia em Português](README.md)

# Exchange Rate Scraping Project

This project performs **web scraping** of exchange rates using the site [www.x-rates.com](https://www.x-rates.com) to retrieve currency information based on a configured list. It formats the data, saves it to a CSV file, and uses a modular structure based on layered architecture.

## Project Architecture

The project follows a **layered architecture**, which makes the codebase easier to maintain and scale. Below is an overview of how the layers and modules are organized:

### Project Structure

```
my_project/
│
├── config/
│   └── currency.py
│
├── data/
│   └── currency_webscraping.py
│
├── domain/
│   └── coin_processor.py
│
├── infrastructure/
│   └── csv_writer.py
│
├── tests/
│   └── test_currency_webscraping.py
│   └── test_coin_processor.py
│   └── test_csv_writer.py
│
├── requirements.txt
└── main.py
```

### Module Description

- **config/currency.py**: List of currencies to be scraped.
- **data/currency_webscraping.py**: Scrapes data from x-rates.com.
- **domain/coin_processor.py**: Processes and formats data for output.
- **infrastructure/csv_writer.py**: Generates the CSV file.
- **tests/**: Unit tests for the main modules.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/JeanVerissimo/webscraping-cambio.git
cd webscraping-cambio
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure your .env file

Create a `.env` file with your API key:

```
CURRENCY_API_KEY=YourKeyHere
```

## Usage

Run the main script:

```bash
python main.py
```

The script will fetch, process, and save the exchange rate data in CSV format.

### Output Example

```
Real,BRL,1,5.847572,14-04-2025
US Dollar,USD,0.171011,1,14-04-2025
Euro,EUR,0.150689,0.881168,14-04-2025
...
```

## Testing

To run the tests:

```bash
python -m unittest discover tests/
```

## License

Project licensed under the MIT License.