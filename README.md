# Web Scraping de Taxas de Câmbio

[🇬🇧 Read in English](README.eng.md)

# Projeto de Web Scraping de Câmbio

Este projeto realiza o **web scraping** de taxas de câmbio usando o site [www.x-rates.com](https://www.x-rates.com) para obter informações de várias moedas, com base na lista configurada. Ele formata os dados, salva as informações em um arquivo CSV e fornece uma estrutura modular baseada na arquitetura em camadas.

## Arquitetura do Projeto

O projeto segue uma **arquitetura em camadas**, o que facilita a manutenção e a escalabilidade do código. Abaixo está uma visão geral de como as camadas e módulos estão organizados:

### Estrutura do Projeto

```
meu_projeto/
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

### Descrição dos Módulos

- **config/currency.py**: Lista das moedas a serem pesquisadas.
- **data/currency_webscraping.py**: Realiza scraping do site x-rates.com.
- **domain/coin_processor.py**: Processa e formata os dados para saída.
- **infrastructure/csv_writer.py**: Gera o arquivo CSV.
- **tests/**: Testes para os principais módulos.

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/JeanVerissimo/webscraping-cambio.git
cd repositorio
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

## Uso

Execute o script principal:

```bash
python main.py
```

O script irá obter, processar e salvar os dados em formato csv.

### Exemplo de saída

```
Real,BRL,1,5.847572,14-04-2025
Dólar Americano,USD,0.171011,1,14-04-2025
Euro,EUR,0.150689,0.881168,14-04-2025
...
```

## Testes

Para rodar os testes:

```bash
python -m unittest discover tests/
```

## Licença

Projeto sob licença MIT.
